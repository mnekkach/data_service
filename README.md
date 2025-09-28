# DataService

`DataService` is a **singleton container** in Python to store and share data across your entire application.

## Features

- Singleton pattern: only one instance exists in the whole application
- Key → list of values storage (each `set()` adds a value)
- Easy to use methods: `set`, `get`, `keys`, `items`, `clear`

## Requirements

- Compatible with **Python ≥ 3.5**.
- [pytest](https://docs.pytest.org/) (only for running unit tests)

Install pytest with:

```bash
pip install pytest
```

Run pytest from the project root
```bash
pytest tests/test_dataservice.py
```


## Installation

Simply copy `dataservice.py` into your project.

## Usage

```python
from dataservice import DataService

# Retrieve the unique instance
ds = DataService()

# Store a value
ds.set("config", {"ip": "192.168.1.1", "port": 5555})

# Retrieve the value
my_config = ds.get("config")[0]
print(my_config["ip"])  # 192.168.1.1
