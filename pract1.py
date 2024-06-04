import sqlite3
import pandas as pd

square = lambda n : n*n;

conn = sqlite3.connect("northwind.db")
conn.create_function("square",1,square)

cursor = conn.cursor()
cursor.execute('''
    SELECT * FROM Products;
    ''')

results=cursor.fetchall()
results_df=pd.DataFrame(results)

conn.commit()

cursor.close()
conn.close()

print(results_df)