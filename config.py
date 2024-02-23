"""User changeable configuration variables"""
from anki.collection import Collection
# IP addresses checked by network_listener()
# Set any IP to check against, public or local
ADDRESSES = [
  "10.0.0.1",
  "8.8.8.8",
  "1.1.1.1"
]

# Maximum number of reboots where a notification will be sent
NOTIFICATIONSCAP = 1
THRESHOLD=5

COLLECTION = Collection(
    "/Users/antonplisnier/Library/Application Support/Anki2/User 1/collection.anki2"
    )
