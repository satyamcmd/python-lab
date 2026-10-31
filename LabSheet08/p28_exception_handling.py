"""
Program 28: Display all database errors using exception handling.

Each test below deliberately causes a different kind of error and shows how
try-except catches it. Specific sqlite3 exceptions are caught first, then the
generic sqlite3.Error as a fallback.
"""
import sqlite3
from db_config import DB_PATH, ensure_students


def run_test(title, action):
    """Run one test function and report any database error it raises."""
    print(f"\n--- {title} ---")
    try:
        action()
        print("No error.")
    except sqlite3.OperationalError as e:
        print("OperationalError (bad SQL / missing table / cannot open DB):", e)
    except sqlite3.IntegrityError as e:
        print("IntegrityError (constraint violated):", e)
    except sqlite3.ProgrammingError as e:
        print("ProgrammingError (wrong use of the API):", e)
    except sqlite3.Error as e:
        print("Other database error:", e)


conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    ensure_students(conn)

    # 1. SQL syntax error
    run_test("Syntax error", lambda: conn.execute("SELEC * FROM students"))

    # 2. Table that does not exist
    run_test("Missing table", lambda: conn.execute("SELECT * FROM no_such_table"))

    # 3. Missing column
    run_test("Missing column", lambda: conn.execute("SELECT salary FROM students"))

    # 4. NOT NULL constraint violation (name is required)
    run_test("NOT NULL violation",
             lambda: conn.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                                  (None, 20, 50)))

    # 5. Duplicate primary key (same id inserted twice; rolled back at the end)
    def duplicate_key():
        sql = "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)"
        conn.execute(sql, (9999, "Duplicate", 20, 50))
        conn.execute(sql, (9999, "Duplicate", 20, 50))  # second insert fails

    run_test("Duplicate primary key", duplicate_key)

    # 6. Wrong number of parameters
    run_test("Wrong parameter count",
             lambda: conn.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Only one",)))

    # 7. Connection failure (folder that does not exist)
    run_test("Connection error",
             lambda: sqlite3.connect("/no/such/folder/test.db"))

    conn.rollback()  # undo any partial work from the failed statements
except sqlite3.Error as e:
    print("Unexpected database error:", e)
finally:
    if conn:
        conn.close()
        print("\nConnection closed.")
