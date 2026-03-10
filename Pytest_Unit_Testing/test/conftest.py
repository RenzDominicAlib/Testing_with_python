import pytest
import sqlite3


@pytest.fixture(scope="module")
def db_connection(request):
    """Create a SQLite database connection for testing."""
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE users
                 (username TEXT, email TEXT)"""
    )
    conn.commit()

    def teardown():
        """Close the database connection after the test."""
        conn.close()

    request.addfinalizer(teardown)
    return conn
