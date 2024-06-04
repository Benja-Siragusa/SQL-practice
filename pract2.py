import sqlite3
import pandas as pd

square = lambda n : n*n;

with sqlite3.connect("northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
    #no hace falta hacer commit ni hacer close para cerrar las conecciones aca por el tipo de acceso que hicimos
print(results_df)