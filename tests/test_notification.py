# Checks that notifications work on whichever browser you are using
from plyer import notification

notification.notify(
    title="Test",
    message="This is a test notification",
    timeout=10
)