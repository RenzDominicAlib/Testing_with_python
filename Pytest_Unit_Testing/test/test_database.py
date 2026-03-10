from Pytest_Unit_Testing.src.database import create_user, update_email


def test_create_user(db_connection):
    """Validate the creation of a new user in the database."""
    create_user(db_connection, "user1", "user1@example.com")
    # Verify the user's presence in the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", ("user1",))
    result = cursor.fetchone()
    print(result)
    assert result is not None  # Confirm the user's existence
    assert result[1] == "user1@example.com"  # Confirm the correct email of the user

def test_update_email(db_connection):
    """Check the update of a user's email in the database."""
    create_user(db_connection, "user2", "user2@example.com")
    update_email(db_connection, "user2", "new_email@example.com")
    # Confirm the email update in the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT email FROM users WHERE username=?", ("user2",))
    result = cursor.fetchone()
    print(result)
    assert result is not None  # Confirm the user's existence
    assert result[0] == "new_email@example.com"  # Confirm the updated email
