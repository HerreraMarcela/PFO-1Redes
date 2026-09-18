import sqlite3

conn = sqlite3.connect("mensajes.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM mensajes")
filas = cursor.fetchall()

print(f"{'ID':<4} | {'FECHA':<20} | {'IP CLIENTE':<12} | {'MENSAJE'}")
print("-" * 60)
for fila in filas:
    print(f"{fila[0]:<4} | {fila[2]:<20} | {fila[3]:<12} | {fila[1]}")

conn.close()