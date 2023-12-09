import pyodbc

# Database Configuration (replace with actual credentials)
SERVER_NAME = 'northuniversityta.database.windows.net'
DATABASE_NAME = 'TA_Management_Suite_DB'
USER_NAME = 'ta_admin'
PASSWORD = 'TA@SecurePass123'
DRIVER = '{ODBC Driver 17 for SQL Server}'


# Connection string
conn_str = f'DRIVER={DRIVER};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={USER_NAME};PWD={PASSWORD}'

def fetch_data_from_database(query, params=None):
    """Fetch data from Azure SQL Database."""
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        return [dict(zip(column_names, row)) for row in rows]

def match_TA_to_course(ta_id):
    """Match a TA to a course based on their skills."""
    # Fetch TA data
    ta_data = fetch_data_from_database("SELECT * FROM TAs WHERE id=?", (ta_id,))
    if not ta_data:
        print(f"No TA found with ID {ta_id}")
        return

    ta = ta_data[0]
    
    # Fetch courses that require the TA's skills
    courses = fetch_data_from_database("SELECT * FROM Courses WHERE required_skill IN (?)", (",".join(ta['skills']),))
    
    if not courses:
        print(f"No matching course found for TA with ID {ta_id}")
        return

    # For this example, just returning the first matching course
    matched_course = courses[0]

    return matched_course

# Example usage
ta_id = 1  # Replace with an actual TA ID from your database
matched_course = match_TA_to_course(ta_id)
if matched_course:
    print(f"TA {ta_id} matched to course {matched_course['course_name']}")

