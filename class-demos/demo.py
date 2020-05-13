# import psycopg2
#
# connection = psycopg2.connect('dbname=example')
#
# cursor = connection.cursor()
#
# cursor.execute('''
#     CREATE TABLE table2 (
#         id INTEGER PRIMARY KEY,
#         completed BOOLEAN NOT NULL DEFAULT False
#     );
# ''')
#
# cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')
#
# connection.commit()
#
# connection.close()
# cursor.close()

# HOW TO FETCH RESULTS IN PSYCOPG2

import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, % (completed)s);'

data = {
    'id': 2,
    'completed': False
}

# cursor.execute(SQL, data) this line of code does not work

cursor.execute('SELECT * from table2;')

result = cursor.fetchall()
print(result)

connection.commit()

connection.close()
cursor.close()
