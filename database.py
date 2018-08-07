import sqlite3


conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE medico (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm INTEGER,
        especialidade TEXT NOT NULL
);
""")

cursor.execute("""CREATE TABLE pacientes(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		nome TEXT NOT NULL,
		cpf INTEGER NOT NULL,
		rg INTEGER NOT NULL,
		sexo TEXT NOT NULL,
		idade INTEGER NOT NULL,
		endereço TEXT NOT NULL,
		telefone TEXT NOT NULL
);
""")

cursor.execute("""CREATE TABLE anamnese(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		data TEXT NOT NULL,
		historico_familiar TEXT NOT NULL,
		historico_da_doenca TEXT NOT NULL,
		doencas_cronicas TEXT NOT NULL,
		alergias TEXT NOT NULL,
		medicamentos TEXT NOT NULL,
		tipo_sanguineo TEXT NOT NULL,	
		observacoes TEXT NOT NULL,
		crm INTEGER NOT NULL,
		rg INTEGER NOT NULL
);
""")

print("Tabelas criadas com sucesso")

conn.close()
