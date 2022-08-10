import sqlite3
conn = sqlite3.connect('db.sqlite3')
conn.execute("DELETE from app1_python where id=21")
cursor = conn.execute("SELECT id, link, title from app1_python")
for id, link, title in cursor:
    print(id, link, 'and ', title)
conn.commit()
conn.close()