
import sqlite3
import hashlib

# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Add a test user
username = "testuser"
email = "test@example.com"
plain_password = "securepassword"
hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()
phone = "1234567890"
cabin = "A101"
status = "Available"
timings = "9 AM - 5 PM"
device = "00:1A:7D:DA:71:11"  # Example MAC address
public_id = "123e4567-e89b-12d3-a456-426614174000"

cursor.execute('''
    INSERT INTO users (username, email, password, phone, cabin, status, timings, device, public_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (username, email, hashed_password, phone, cabin, status, timings, device, public_id))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Test user added successfully!")
