from azure.identity import DefaultAzureCredential
from azure.mgmt.notificationhubs import NotificationHubsManagementClient

# Azure Configuration

SUBSCRIPTION_ID = 'a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6'
RESOURCE_GROUP_NAME = 'NorthUniversityTA_ResourceGroup'
NAMESPACE_NAME = 'NorthUnivTA_NotificationHubNS'
HUB_NAME = 'TA_Assignment_Notifications'


# Authentication with Azure
credential = DefaultAzureCredential()

# Create a client instance
notification_client = NotificationHubsManagementClient(credential, SUBSCRIPTION_ID)

def send_in_app_notification(tag, message):
    """Send in-app notification using Azure Notification Hub."""

    android_payload = f"""{{ "data" : {{"message":"{message}"}} }}"""

    # Send the message
    notification_client.notification_hubs.send(
        RESOURCE_GROUP_NAME, 
        NAMESPACE_NAME, 
        HUB_NAME, 
        {
            "message": android_payload,
            "tags": tag  # e.g., 'student:1234' to target a specific student
        }
    )

# Example usage:
send_in_app_notification('student:1234', 'You have been assigned to CS101.')
