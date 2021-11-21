# Importa a biblioteca do Sqlite3 Database
import sqlite3

# Cria o Database SQLite 'UserData.db'
conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

# Cria a tabela Users que receberá os dados da conta do usuário.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

# Print
print("Conectado ao Banco de Dados")