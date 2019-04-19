import pyodbc

conn  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:yunzhucsdev.database.chinacloudapi.cn,1433;UID=yzsqlcsdev;PWD=tz5566_6633;Database=System;')
cursor = conn.cursor()
cursor.execute('select * from SYSTEM_FEATURE')
rows = cursor.fetchall()
for row in rows:
    print(row,1)