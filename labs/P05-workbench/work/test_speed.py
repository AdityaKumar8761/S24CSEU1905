
"""My own tests for minutes_per_km."""

import pytest

from orders import minutes_per_km


def test_slow_delivery():
    """Test minutes_per_km with a valid distance."""

    # 60 minutes for 6 km = 10 minutes per km
    assert minutes_per_km(60, 6) == 10.0


def test_negative_distance_raises():
    """Test that negative distance raises ValueError."""

    # Negative distance should raise ValueError
    with pytest.raises(ValueError):
        minutes_per_km(60, -3)
