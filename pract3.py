import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("northwind.db")
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.Productid = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_product= pd.read_sql_query(query,conn)
#print(top_product)

top_product.plot(x="ProductName",y="Revenue",kind="bar",figsize=(10,5),legend=0)

plt.title("10 products mas rentables")
plt.xlabel("productos")
plt.ylabel("revenue")
plt.xticks(rotation=90)
plt.show()

query2 = '''
    SELECT FirstName || " " || LastName AS Employee, COUNT(*) as total
    FROM Orders O
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY total DESC
'''

top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="Employee",y="total",kind="bar",figsize=(10,5),legend=False)
plt.title("empleados mas efectivos")
plt.xlabel("empleado")
plt.ylabel("total vendido")
plt.xticks(rotation=45)
plt.show()