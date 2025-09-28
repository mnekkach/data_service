import pytest
from ..DataService import DataService


@pytest.fixture
def ds():
    """Return a fresh DataService instance before each test."""
    # Ensure container is cleared before each test
    instance = DataService()
    instance.clear()
    return instance


def test_singleton_instance(ds):
    """Test that DataService returns the same instance (singleton pattern)."""
    ds2 = DataService()
    assert ds is ds2, "DataService should always return the same instance."


def test_set_and_get_value(ds):
    """Test setting and getting a value from DataService."""
    sample_data = {"ip": "127.0.0.1", "port": 8080}
    ds.set("config", sample_data)
    retrieved = ds.get("config")
    assert isinstance(retrieved, list), "Stored values should be in a list."
    assert retrieved[0] == sample_data, "Retrieved value should match the stored value."


def test_multiple_values_same_key(ds):
    """Test adding multiple values under the same key."""
    ds.set("numbers", 1)
    ds.set("numbers", 2)
    values = ds.get("numbers")
    assert values == [1, 2], "Values under the same key should accumulate in a list."


def test_get_default_value(ds):
    """Test getting a default value when key does not exist."""
    default_value = {"default": True}
    result = ds.get("nonexistent", default=default_value)
    assert result == default_value, "Should return the default value if key not found."


def test_clear_container(ds):
    """Test clearing the container."""
    ds.set("key1", "value1")
    ds.set("key2", "value2")
    ds.clear()
    assert len(list(ds.keys())) == 0, "Container should be empty after clear()."


def test_keys_and_items(ds):
    """Test keys() and items() views."""
    ds.set("a", 1)
    ds.set("b", 2)
    keys = list(ds.keys())
    assert "a" in keys and "b" in keys, "keys() should return all keys."
    items = list(ds.items())
    assert any(k == "a" for k, _ in items), "items() should return (key, value) pairs."
