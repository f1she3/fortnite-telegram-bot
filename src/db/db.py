"""
    This module handles the interactions with the sqlite3 database.
"""

import sqlite3
import os
from handlers import constants

def db_init():
    """
    Initialize the SQLite database at the specified path.
    If the database already exists, return True.
    If the database does not exist, create it and return True.
    """
    init_path=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        "init.sql"
    )
    if not os.path.exists(constants.DB_ABS_PATH):
        # Database does not exist, create it
        conn = sqlite3.connect(constants.DB_ABS_PATH)
        cursor = conn.cursor()

        # Read the SQL commands from the init.sql file
        with open(init_path, "r", encoding="utf-8") as f:
            query = f.read()
            # Execute the SQL commands
            cursor.execute(query)


        # Commit the changes and close the connection
        conn.commit()
        conn.close()

def db_get_all_rows(table_name:str):
    """
    Retrieve all rows from the specified table in the SQLite database
    and return them as a list of dictionaries, where each dictionary
    represents a row and has keys corresponding to the column names.
    """
    conn = sqlite3.connect(constants.DB_ABS_PATH)
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM {table_name}')

    # Get the column names from the cursor description
    column_names = [
        desc[0] for desc in cursor.description
    ]

    # Fetch all rows from the cursor and convert them to a list of dictionaries
    rows = [
        dict(
            zip(column_names, row)
        ) for row in cursor.fetchall()
    ]

    conn.close()

    return rows

def db_update_stats(
        tg_id:int,
        new_kill_count:int,
        new_death_count:int,
        new_match_count:int
):
    """
    Update a player's stats.
    """
    conn = sqlite3.connect(constants.DB_ABS_PATH)
    cursor = conn.cursor()
    query = "UPDATE players SET kills=?, deaths=?, matches=? WHERE tg_id=?"
    values = (
        new_kill_count,
        new_death_count,
        new_match_count,
        tg_id
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def db_add_player(tg_id:int, fortnite_username:str):
    """
    Update a player's stats.
    """
    conn = sqlite3.connect(constants.DB_ABS_PATH)
    cursor = conn.cursor()
    query = """
    INSERT INTO players (tg_id, fortnite_username)
    VALUES (?, ?)
    """
    # Create a tuple of values for the prepared statement
    values = (tg_id, fortnite_username)

    # Execute the prepared statement with the values
    cursor.execute(query, values)
    conn.commit()
    conn.close()
