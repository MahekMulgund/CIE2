# test_speed.py
import pytest
from speed import calculate_speed  # change 'your_module' to your actual filename

def test_calculate_speed():
    # Normal cases
    assert calculate_speed(100, 2) == 50
    assert calculate_speed(20, 1) == 20

def test_calculate_speed_zero_time():
    # Expecting ValueError when time is zero
    with pytest.raises(ValueError):
        calculate_speed(100, 0)

def test_calculate_speed_negative_time():
    # Expecting ValueError when time is negative
    with pytest.raises(ValueError):
        calculate_speed(100, -1)
