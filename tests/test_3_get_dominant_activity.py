from acc_activity import get_dominant_activity


file0_activity_signal = ['moving', 'moving', 'moving', 'moving', 'standing', 'standing', 'moving', 'lying']
file0_dominant_activity = 'moving'

file1_activity_signal = ['standing', 'standing', 'standing', 'standing', 'standing', 'standing', 'moving', 'lying', 'lying', 'lying']
file1_dominant_activity = 'standing'

example_activity_signal = ['standing', 'standing', 'standing', 'moving', 'standing', 'lying']
example_dominant_activity = 'standing'


def test_get_dominant_activity():
    assert get_dominant_activity(example_activity_signal) == example_dominant_activity
    assert get_dominant_activity(file0_activity_signal) == file0_dominant_activity
    assert get_dominant_activity(file1_activity_signal) == file1_dominant_activity