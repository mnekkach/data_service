from typing import Any, Optional, Dict

class DataService:
    """
    DataService is a **singleton container**.
    Only one instance exists for the entire application.

    It allows you to store and retrieve centralized data via keys.
    Each key contains a **list of values** (each call to `set()` adds a new value).
    """

    # Unique instance of the singleton
    _instance: Optional['DataService'] = None
    # Internal dictionary used as storage
    _storage: Dict[str, Any]

    def __new__(cls):
        """
        Special method called when creating a new instance.
        Creates or returns the unique DataService instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._storage = {}
            print(f"[INFO] New instance of DataService has been created {cls._instance}.")
        else:
            print(f"[INFO] An instance of DataService already exists. "
                  f"\n\t   The new instance is the same as the existing {cls._instance}.")
        return cls._instance

    def set(self, key: str, value: Any) -> None:
        """
        Add a value under the specified key.

        If the key does not exist yet, it is initialized with an empty list,
        then the value is appended to this list.

        Parameters
        ----------
        key : str
            The key used to identify the stored data.
        value : Any
            The value to store.
        """
        if key not in self._storage:
            self._storage[key] = []
        self._storage[key].append(value)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value by its key.

        Parameters
        ----------
        key : str
            The key used to identify the stored data.
        default : Any, optional
            The value returned if the key does not exist (default: None).

        Returns
        -------
        Any
            The stored value under the key or `default` if it does not exist.
        """
        return self._storage.get(key, default)

    def clear(self) -> None:
        """
        Completely clear the container.
        """
        return self._storage.clear()

    def keys(self):
        """
        Return a view object of all stored keys.
        """
        return self._storage.keys()

    def items(self):
        """
        Return a view object of all (key, value) pairs.
        """
        return self._storage.items()


if __name__ == "__main__":
    # Example usage
    my_data_service = DataService()
    my_data_service2 = DataService()

    # Example data
    datas = {"config": "default",
             "ip": "192.168.1.1",
             "port": "5555"}

    # Store data in DataService with a custom key
    my_data_service.set("configuration.key", datas)

    # Retrieve data with the custom key
    my_configuration = my_data_service.get("configuration.key")

    # Display data
    print("==== Configuration ====")
    the_config = my_configuration[0]
    print(f"Configuration :: {the_config['config']}")
    print(f"Ip address :: {the_config['ip']}")
    print(f"Port :: {the_config['port']}")
    print("=======================")
