-- Users Table
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username NVARCHAR(50) NOT NULL,
    Password NVARCHAR(255) NOT NULL,  -- Assuming hashed password
    Email NVARCHAR(100) NOT NULL,
    Role NVARCHAR(50) NOT NULL
);

-- UserProfile Table
CREATE TABLE UserProfile (
    UserProfileID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    ContactNumber NVARCHAR(15),
    Address NVARCHAR(255),
    AdditionalInformation NVARCHAR(MAX)
);

-- Courses Table
CREATE TABLE Courses (
    CourseID INT IDENTITY(1,1) PRIMARY KEY,
    CourseCode NVARCHAR(20) NOT NULL,
    CourseName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(MAX),
    InstructorID INT FOREIGN KEY REFERENCES Users(UserID),
    TARequired BIT NOT NULL
);

-- Applications Table
CREATE TABLE Applications (
    ApplicationID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    CourseID INT FOREIGN KEY REFERENCES Courses(CourseID),
    CV NVARCHAR(MAX),  -- File path or URL to the CV
    Status NVARCHAR(50) NOT NULL,
    SubmissionDate DATETIME NOT NULL
);

-- TAExperience Table
CREATE TABLE TAExperience (
    ExperienceID INT IDENTITY(1,1) PRIMARY KEY,
    ApplicationID INT FOREIGN KEY REFERENCES Applications(ApplicationID),
    CourseName NVARCHAR(100),
    Institution NVARCHAR(100),
    StartDate DATE,
    EndDate DATE
);

-- CourseAssignments Table
CREATE TABLE CourseAssignments (
    AssignmentID INT IDENTITY(1,1) PRIMARY KEY,
    CourseID INT FOREIGN KEY REFERENCES Courses(CourseID),
    TAUserID INT FOREIGN KEY REFERENCES Users(UserID),
    Term NVARCHAR(20),
    Year INT
);

-- TAReviews Table
CREATE TABLE TAReviews (
    ReviewID INT IDENTITY(1,1) PRIMARY KEY,
    AssignmentID INT FOREIGN KEY REFERENCES CourseAssignments(AssignmentID),
    InstructorID INT FOREIGN KEY REFERENCES Users(UserID),
    Rating INT,
    Comments NVARCHAR(MAX),
    DateOfReview DATETIME
);

-- Notifications Table
CREATE TABLE Notifications (
    NotificationID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    Type NVARCHAR(50),
    Message NVARCHAR(MAX),
    DateSent DATETIME
);

-- AuditLogs Table
CREATE TABLE AuditLogs (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    ActionType NVARCHAR(50),
    Description NVARCHAR(MAX),
    Timestamp DATETIME DEFAULT GETDATE()
);
