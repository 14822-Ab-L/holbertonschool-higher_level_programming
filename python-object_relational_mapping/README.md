# Python - Object-relational Mapping

This directory contains Python exercises focused on connecting to MySQL databases and using SQLAlchemy to work with database tables through Python objects.

## Topics

- MySQL database connections
- Querying databases with `MySQLdb`
- Filtering database results
- SQL injection prevention
- Object-relational mapping (ORM)
- SQLAlchemy models and sessions
- Mapping Python classes to database tables
- Retrieving, inserting, updating, and deleting records
- Foreign keys and relationships between tables

## Files and Description

| **File** | **Description** |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `0-select_states.py` | Lists all states from a MySQL database in ascending ID order. |
| `1-filter_states.py` | Lists states whose names begin with an uppercase `N`. |
| `2-my_filter_states.py` | Lists states matching a name supplied as a command-line argument. |
| `3-my_safe_filter_states.py` | Filters states by name using a query that protects against SQL injection. |
| `4-cities_by_state.py` | Lists cities with their associated state names. |
| `5-filter_cities.py` | Lists the cities belonging to a specified state. |
| `model_state.py` | Defines the SQLAlchemy `State` model for the `states` table. |
| `7-model_state_fetch_all.py` | Retrieves and displays all `State` objects ordered by ID. |
| `8-model_state_fetch_first.py` | Retrieves and displays the first `State` object by ID. |
| `9-model_state_filter_a.py` | Lists `State` objects whose names contain the letter `a`. |
| `10-model_state_my_get.py` | Retrieves a state by name and displays its ID. |
| `11-model_state_insert.py` | Adds a new `State` object to the database. |
| `12-model_state_update_id_2.py` | Updates the name of the state with ID 2. |
| `13-model_state_delete_a.py` | Deletes `State` objects whose names contain the letter `a`. |
| `model_city.py` | Defines the SQLAlchemy `City` model and its relationship to the `states` table. |
| `14-model_city_fetch_by_state.py` | Retrieves cities with their associated state names, ordered by city ID. |
