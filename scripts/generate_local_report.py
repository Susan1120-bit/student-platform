from app import get_db, build_excel, _analyze_one_submission

conn = get_db()
latest = conn.execute('''
    SELECT student_email, MAX(id) AS latest_id
    FROM submissions
    WHERE sent = 0
    GROUP BY student_email
''').fetchall()
if not latest:
    print('No new submissions to process')
    conn.close()
    raise SystemExit(0)
latest_ids = [row['latest_id'] for row in latest]
questions_list = [dict(q) for q in conn.execute('SELECT * FROM questions ORDER BY order_num, id').fetchall()]
conn.close()

for sid in latest_ids:
    print(f'Analyzing submission {sid}...')
    _analyze_one_submission(sid, questions_list)

print('Building Excel...')
excel = build_excel(latest_ids)
if not excel:
    print('Could not build Excel')
else:
    with open('submissions_test.xlsx', 'wb') as f:
        f.write(excel)
    print('Wrote submissions_test.xlsx')
