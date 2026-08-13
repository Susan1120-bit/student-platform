import sqlite3

DB = 'database.db'

questions = [
    ("Palindrome Check",
     "Return True if the input string is a palindrome when ignoring non-alphanumeric characters and case.",
     "def is_palindrome(s):",
     1),
    ("Nth Fibonacci",
     "Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1). n is a non-negative integer.",
     "def fib(n):",
     2),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()
for title, desc, template, order in questions:
    cur.execute('SELECT id FROM questions WHERE title=?', (title,))
    if cur.fetchone():
        print(f"Skipped existing: {title}")
    else:
        cur.execute('INSERT INTO questions (title, description, template, order_num) VALUES (?,?,?,?)',
                    (title, desc, template, order))
        print(f"Inserted: {title}")

conn.commit()
conn.close()
print('Done')
