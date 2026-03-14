import sqlite3

def setup_database():
    # Connect to SQLite (this automatically creates the database file)
    conn = sqlite3.connect("qa_bugs.db")
    cursor = conn.cursor()
    
    # Create the relational database table for QA Bugs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bugs (
            bug_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            priority TEXT NOT NULL
        )
    ''')
    
    # Insert a sample test-case bug using SQL
    cursor.execute('''
        INSERT INTO bugs (description, status, priority) 
        VALUES ('Login button fails on mobile screen', 'Open', 'High')
    ''')
    
    # Save the changes
    conn.commit()
    
    # Query (SELECT) and display the logs
    print("--- Current QA Bug Tracker Logs ---")
    cursor.execute("SELECT * FROM bugs")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Bug: {row[1]} | Status: {row[2]} | Priority: {row[3]}")
        
    conn.close()

if __name__ == "__main__":
    setup_database()
