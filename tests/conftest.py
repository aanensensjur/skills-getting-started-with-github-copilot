import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def restore_activity_participants():
    original_participants = {
        name: list(activity["participants"])
        for name, activity in activities.items()
    }

    yield

    for name, participants in original_participants.items():
        activities[name]["participants"] = participants
