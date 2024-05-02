from unittest.mock import Mock
from lib.exercise.time_error import TimeError

def test_calls_api_returns_json():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "unixtime": 1668262850
    }
    timer_mock = Mock()
    timer_mock.time.return_value = 1668262850.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5
    
    