

def create_user(conn, username, email):
    """Create a new user in the database."""
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, email))
    conn.commit()


def update_email(conn, username, new_email):
    """Update user's email in the database."""
    c = conn.cursor()
    c.execute("UPDATE users SET email = ? WHERE username = ?", (new_email, username))
    conn.commit()
