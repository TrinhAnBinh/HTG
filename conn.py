import cx_Oracle

db_conn = cx_Oracle.connect('TRINGUYENH/password_htg@//103.163.214.72:1521/XEPDB1', encoding = "UTF-8")
cursor = db_conn.cursor()
cursor.execute('SELECT * FROM T_D_ACCOUNT_TYPE')

print(cursor.fetchall())