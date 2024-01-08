import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="123")
connection_cursor = connection.cursor()
connection_cursor.execute("""CREATE TABLE IF NOT EXISTS test_table (a bytea, b int, c text);""")

""" with open('./a.out', 'rb') as f: """
"""     bin_data = f.read() """
""""""
""" connection_cursor.execute('''INSERT INTO test_table VALUES (%s, 1337, 'foo')''', (bin_data,)) """
""" connection_cursor.execute('''UPDATE test_table SET a = %s''', (bin_data + b'1',)) """

connection_cursor.execute("SELECT a FROM test_table WHERE b = %s", (1337,)) 
data = connection_cursor.fetchone()[0]

with open('./new.out', 'wb') as f: 
    f.write(data) 


