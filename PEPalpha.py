from tkinter import *
import sqlite3


global conn

conn = sqlite3.connect("data.db")

global cursor

cursor = conn.cursor()

def root_specs(janela): #Propriedades da janela principal
	lb1 = Label(janela, bg = "black")
	lb2 = Label(janela, bg = "black")
	lb3 = Label(janela, bg = "black")
	lb1.grid(row = 1, column = 2)
	lb2.grid(row = 1, column = 4)
	lb3.grid(row = 3, column = 1)
	janela.title("Prontuário Eletrônico de Pacientes")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("350x150+100+100")

def cadastro_medico_specs(janela): #Propriedades da janela de Cadastro Medico
	
	janela.title("Cadastro do Médico")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("280x120+200+200")

def cadastro_pacientes_specs(janela): #Propriedades da janela de Cadastro do Paciente
	
	janela.title("Cadastro do Paciente")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("280x180+200+200")

def cadastro_anamnese_specs(janela): #Propriedades da janela de Cadastro da Anamnese
	
	janela.title("Cadastro da Anamnese")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("320x250+200+200")

def pesquisar_medico_specs(janela): #Propriedades da janela de Pesquisar Medico
	
	janela.title("Pesquisar Médico")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("230x110+100+100")

def pesquisar_paciente_specs(janela): #Propriedades da janela de Pesquisar Paciente
	
	janela.title("Pesquisar Paciente")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("230x190+100+100")

def pesquisar_anamnese_specs(janela): #Propriedades da janela de Pesquisar Anamnese
	
	janela.title("Pesquisar Anamnese")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("255x100+100+100")



def cadastro_medico(): # Janela de Cadastro Medico
	janela = Tk()
	cadastro_medico_specs(janela) 
	
	global nomemed
	global crmmed
	global especialidademed

	lbnome = Label(janela, fg="Green", bg="black", text="Nome: ")
	nomemed = Entry(janela, fg="GREEN", bg="Black")
	lbcrm = Label(janela, fg="Green", bg="black", text="CRM: ")
	crmmed = Entry(janela, fg="GREEN", bg = "black")
	lbespecialidade = Label(janela, fg="green", bg = "black", text="Esp: ")
	especialidademed = Entry(janela, fg="green", bg="black")
	

	lbnome.grid(row = 1, column = 1)
	nomemed.grid(row = 1, column = 2)
	
	lbcrm.grid(row = 2, column = 1)
	crmmed.grid(row = 2, column = 2)

	lbespecialidade.grid(row = 3, column = 1)
	especialidademed.grid(row = 3, column = 2)


	btsave = Button(janela, bg="black", fg="green", text = "SALVAR", command=click_salvar_medico)
	btsave.grid(row = 5, column = 2)

	janela.mainloop()

def click_salvar_medico(): # Função para inserir entrada no BD

	nome = nomemed.get()
	crm = crmmed.get()
	especialidade = especialidademed.get()

	cursor.execute("""
		INSERT INTO medico (CRM, Nome, Especialidade)
		VALUES(?,?,?) """, (crm, nome, especialidade))
	
	conn.commit()

	print("Dados do Médico cadastrados com sucesso!")


def cadastro_paciente(): # Janela de Cadastro de Pacientes
	janela = Tk()
	cadastro_pacientes_specs(janela)

	global nomepac
	global cpfpac
	global rgpac
	global sexopac
	global endpac
	global idadepac
	global telefonepac

	lbnome = Label(janela, fg="Green", bg="black", text="Nome: ")
	nomepac = Entry(janela, fg="GREEN", bg="Black")
	lbcpf = Label(janela, fg="Green", bg="black", text="CPF: ")
	cpfpac = Entry(janela, fg="GREEN", bg = "black")
	lbrg = Label(janela, fg="green", bg = "black", text="RG: ")
	rgpac = Entry(janela, fg="green", bg="black")
	lbsexo = Label(janela, fg="green", bg = "black", text="Sexo: ")
	sexopac = Entry(janela, fg="green", bg="black")
	lbend = Label(janela, fg="Green", bg="black", text="Endereço: ")
	endpac = Entry(janela, fg="GREEN", bg="Black")
	lbidade = Label(janela, fg="Green", bg="black", text="Idade: ")
	idadepac = Entry(janela, fg="GREEN", bg="Black")
	lbtelefone = Label(janela, fg="Green", bg="black", text="Telefone: ")
	telefonepac = Entry(janela, fg="GREEN", bg="Black")

	lbnome.grid(row = 1, column = 1)
	nomepac.grid(row = 1, column = 2)
	
	lbcpf.grid(row = 2, column = 1)
	cpfpac.grid(row = 2, column = 2)

	lbrg.grid(row = 3, column = 1)
	rgpac.grid(row = 3, column = 2)

	lbsexo.grid(row = 4, column = 1)
	sexopac.grid(row = 4, column = 2)

	lbidade.grid(row = 5, column = 1)
	idadepac.grid(row = 5, column = 2)

	lbend.grid(row = 6, column = 1)
	endpac.grid(row = 6, column = 2)

	lbtelefone.grid(row = 7, column = 1)
	telefonepac.grid(row = 7, column = 2)

	btsave = Button(janela, bg="black", fg="green", text = "SALVAR", command=click_salvar_paciente)
	btsave.grid(row = 8, column = 2)

	janela.mainloop()

def click_salvar_paciente(): # Função para inserir entrada no BD

	nome = nomepac.get()
	cpf = cpfpac.get()
	rg = rgpac.get()
	sex = sexopac.get()
	idade = idadepac.get()
	endereço = endpac.get()
	telefone = telefonepac.get()

	cursor.execute("""
		INSERT INTO paciente (RG, Nome, CPF, Sexo, Idade, End, Tel)
		VALUES(?,?,?,?,?,?,?) """, (rg, nome, cpf, sex, idade, endereço, telefone))
	
	conn.commit()

	print("Informações cadastrados com sucesso!")


def cadastro_anamnese(): # Janela de Cadastro de Anamnese
	janela = Tk()
	cadastro_anamnese_specs(janela)

	lbpcrm = Label(janela, bg="black", fg="green", text="CRM do Medico: ")
	lbprg = Label(janela, bg="black", fg="green", text="RG do Paciente: ")
	lbp1 = Label(janela, bg="black", fg="green", text="Data (DD/MM/AA):	   ")
	lbp2 = Label(janela, bg="black", fg="green", text="Histórico Familiar: ")
	lbp3 = Label(janela, bg="black", fg="green", text="Histórico da Doença: ")
	lbp4 = Label(janela, bg="black", fg="green", text="Doenças Crônicas: ")
	lbp5 = Label(janela, bg="black", fg="green", text="Alergias: ")
	lbp6 = Label(janela, bg="black", fg="green", text="Medicamentos: ")
	lbp7 = Label(janela, bg="black", fg="green", text="Tipo Sanguíneo: ")
	lbp8 = Label(janela, bg="black", fg="green", text="Resultado: ")

	global pcrm
	global prg
	global p1
	global p2
	global p3
	global p4
	global p5
	global p6
	global p7
	global p8


	pcrm = Entry(janela, bg="black", fg="green")
	prg = Entry(janela, bg="black", fg="green")
	p1 = Entry(janela, bg="black", fg="green")
	p2 = Entry(janela, bg="black", fg="green")
	p3 = Entry(janela, bg="black", fg="green")
	p4 = Entry(janela, bg="black", fg="green")
	p5 = Entry(janela, bg="black", fg="green")
	p6 = Entry(janela, bg="black", fg="green")
	p7 = Entry(janela, bg="black", fg="green")
	p8 = Entry(janela, bg="black", fg="green")

	lbp1.grid(row = 1, column = 1)
	p1.grid(row = 1, column =2)
	
	lbp2.grid(row = 2, column = 1)
	p2.grid(row = 2, column = 2)

	lbp3.grid(row = 3, column = 1)
	p3.grid(row = 3, column = 2)

	lbp4.grid(row = 4, column = 1)
	p4.grid(row = 4, column = 2)

	lbp5.grid(row = 5, column = 1)
	p5.grid(row = 5, column = 2)

	lbp6.grid(row = 6, column = 1)
	p6.grid(row = 6, column = 2)

	lbp7.grid(row = 7, column = 1)
	p7.grid(row = 7, column = 2)

	lbp8.grid(row = 8, column = 1)
	p8.grid(row = 8, column = 2)

	lbpcrm.grid(row = 9, column = 1)
	pcrm.grid(row = 9, column = 2)

	lbprg.grid(row = 10, column = 1)
	prg.grid(row = 10, column = 2)

	btsave = Button(janela, bg="black", fg="green", text="SALVAR", command=click_salvar_anamnese)
	btsave.grid(row = 11, column = 2)

	janela.mainloop()

def click_salvar_anamnese(): # Função para inserir entrada na tabela anamnese

	data = p1.get()
	histfam = p2.get()
	histdoen = p3.get()
	doencron = p4.get()
	alerg = p5.get()
	medicam = p6.get()
	tsang = p7.get()
	result = p8.get()
	crm = pcrm.get()
	rg = prg.get()

	cursor.execute("""
		INSERT INTO anamnese (data,historico_familiar, historico_doenca, doencas_cronicas, alergias, medicamentos, tipo_sanguineo, crm, rg, resultado)
		VALUES(?,?,?,?,?,?,?,?,?,?) """, (data, histfam, histdoen, doencron, alerg, medicam, tsang, crm, rg, result))
	
	conn.commit()

	print("Anamnese cadastrada com sucesso!")


def pesquisar_medico(): # Janela para Pesquisar Medicos
	janela = Tk()
	pesquisar_medico_specs(janela)

	global crmpmed
	global lbblankpmed1 
	global lbblankpmed2 
	global lbblankpmed3

	lbcrm = Label(janela, fg="green", bg="black", text="CRM: ")
	crmpmed = Entry(janela, fg="green", bg="black")
	lbmednome = Label(janela, fg="green", bg="black", text="Nome: ")
	lbmedesp = Label(janela, fg="green", bg="black", text="CRM: ")
	lbmedcrm = Label(janela, fg="green", bg="black", text="Esp: ")
	btsch = Button(janela, text="Pesquisar", bg="black", fg="green", command=click_pesquisar_medico)
	
	lbblankpmed1 = Label(janela, bg="black", fg="green", text="")
	lbblankpmed2 = Label(janela, bg="black", fg="green", text="")
	lbblankpmed3 = Label(janela, bg="black", fg="green", text="")

	lbcrm.grid(row = 1, column = 1)
	crmpmed.grid(row = 1, column = 2)
	btsch.grid(row = 2, column = 2)

	lbmednome.grid(row = 4, column = 1)
	lbmedcrm.grid(row = 5, column = 1)
	lbmedesp.grid(row = 6, column = 1)
	lbblankpmed1.grid(row = 4, column = 2)
	lbblankpmed2.grid(row = 5, column = 2)
	lbblankpmed3.grid(row = 6, column = 2)

	janela.mainloop()

def click_pesquisar_medico(): # Função para pesquisar entrada na tabela medico

	crm = crmpmed.get()
	c = cursor
	c.execute("""SELECT * FROM medico WHERE CRM=?""", [crm])
	output = c.fetchall()

	lbblankpmed1.config(text=output[0][1])
	lbblankpmed2.config(text=output[0][2])
	lbblankpmed3.config(text=output[0][0])

def pesquisar_paciente(): # Janela para Pesquisar Pacientes
	janela = Tk()
	pesquisar_paciente_specs(janela)

	global rgpmed
	global lbblankpac1
	global lbblankpac2
	global lbblankpac3
	global lbblankpac4
	global lbblankpac5
	global lbblankpac6
	global lbblankpac7

	lbrg = Label(janela, fg="green", bg="black", text="RG: ")
	rgpmed = Entry(janela, fg="green", bg="black")

	btsch = Button(janela, text="Pesquisar", bg="black", fg="green", command=click_pesquisar_pacientes)

	lbrg.grid(row = 1, column = 1)
	rgpmed.grid(row = 1, column = 2)
	btsch.grid(row = 2, column = 2)
	lbblankppac = Label(bg="black", fg="black").grid(row = 3, column = 1, columnspan = 2)

	lbnomepac = Label(janela, bg="black", fg="green", text="Nome: ").grid(row = 4, column = 1)
	lbcpfpac = Label(janela, bg="black", fg="green", text="CPF: ").grid(row = 5, column = 1)
	lbrgpac = Label(janela, bg="black", fg="green", text="RG: ").grid(row = 6, column = 1)
	lbsexpac = Label(janela, bg="black", fg="green", text="Sexo: ").grid(row = 7, column = 1)
	lbidadepac = Label(janela, bg="black", fg="green", text="Idade: ").grid(row = 8, column = 1)
	lbendpac = Label(janela, bg="black", fg="green", text="End: ").grid(row = 9, column = 1)
	lbtelpac = Label(janela, bg="black", fg="green", text="Tel: ").grid(row = 10, column = 1)

	lbblankpac1 = Label(janela, bg="black", fg="green", text="")
	lbblankpac1.grid(row = 4, column = 2)
	lbblankpac2 = Label(janela, bg="black", fg="green", text="")
	lbblankpac2.grid(row = 5, column = 2)
	lbblankpac3 = Label(janela, bg="black", fg="green", text="")
	lbblankpac3.grid(row = 6, column = 2)
	lbblankpac4 = Label(janela, bg="black", fg="green", text="")
	lbblankpac4.grid(row = 7, column = 2)
	lbblankpac5 = Label(janela, bg="black", fg="green", text="")
	lbblankpac5.grid(row = 8, column = 2)
	lbblankpac6 = Label(janela, bg="black", fg="green", text="")
	lbblankpac6.grid(row = 9, column = 2)
	lbblankpac7 = Label(janela, bg="black", fg="green", text="")
	lbblankpac7.grid(row = 10, column = 2)

	janela.mainloop()

def click_pesquisar_pacientes(): # Função para pesquisar entrada na tabela pacientes

	rg = rgpmed.get()
	c = cursor
	c.execute("""SELECT * FROM paciente WHERE RG=?""", [rg])
	output = c.fetchall()

	lbblankpac3.config(text=output[0][0])
	lbblankpac1.config(text=output[0][1])
	lbblankpac2.config(text=output[0][2])
	lbblankpac4.config(text=output[0][3])
	lbblankpac5.config(text=output[0][4])
	lbblankpac6.config(text=output[0][5])
	lbblankpac7.config(text=output[0][6])


def pesquisar_anamnese(): # Janela para Pesquisar Anamnese
	janela = Tk()
	pesquisar_anamnese_specs(janela)

	global rgpanm
	global crmpanm
	

	lbrg = Label(janela, fg="green", bg="black", text="RG: ")
	rgpanm = Entry(janela, fg="green", bg="black")

	lbor = Label(janela, fg="green", bg="black", text="OU")

	lbcrm = Label(janela, fg="green", bg="black", text="CRM: ")
	crmpanm = Entry(janela, fg="green", bg="black")

	btsch = Button(janela, text="Pesquisar", bg="black", fg="green", command=click_pesquisar_anamnese)

	lbrg.grid(row = 1, column = 1)
	rgpanm.grid(row = 1, column = 2)
	lbor.grid(row = 2, column = 2)
	lbcrm.grid(row = 3, column = 1)
	crmpanm.grid(row = 3, column = 2)
	btsch.grid(row = 4, column = 2)





	janela.mainloop()

def click_pesquisar_anamnese(): # Função para pesquisar entrada na tabela anamnese

	rg = rgpanm.get()
	crm = crmpanm.get()
	c = cursor
	c.execute("""SELECT * FROM anamnese WHERE  RG = ? OR CRM = ?""", [rg, crm])
	output = c.fetchall()
	
	contador = len(output)
	i = 0
	j = 0
	print ("Anamneses: ")
	for i in range (contador):
		print ("Data: ", output[i][0])
		print ("Hist. Familiar: ", output[i][1])
		print ("Hist. Doença:", output[i][2])
		print ("Doen. Crônic: ", output[i][3])
		print ("Alergias: ", output[i][4])
		print ("Medicamento: ", output[i][5])
		print ("Tipo Sang.: ", output[i][6])
		print ("CRM: ", output[i][7])
		print ("RG: ", output[i][8])
		print ("Resultado: ",output[i][9],"\n")



		

def root_widgets(janela): # Botoes da respectiva janela
	

	btcmed = Button(root, width=10, text="Cadastro\nMédico", bg="black", bd=1, fg="GREEN", command=cadastro_medico)
	btcmed.grid(row = 2, column = 1)

	btcpac = Button(root, width=10, text="Cadastro\nPacientes", bg="black", bd=1, fg="GREEN", command=cadastro_paciente)
	btcpac.grid(row = 2, column = 3)

	btcana = Button(root, width=10, text="Cadastro\nAnamnese", bg="black", bd=1, fg="GREEN", command=cadastro_anamnese)
	btcana.grid(row = 2, column = 5)

	btpmed = Button(root, width=10, text="Pesquisar\nMédico", bg="black", bd=1, fg="GREEN", command=pesquisar_medico)
	btpmed.grid(row = 4, column = 1)

	btppac = Button(root, width=10, text="Pesquisar\nPaciente", bg="black", bd=1, fg="GREEN", command=pesquisar_paciente)
	btppac.grid(row = 4, column = 3)

	btpana = Button(root, width=10, text="Pesquisar\nAnamnese", bg="black", bd=1, fg="GREEN", command=pesquisar_anamnese)
	btpana.grid(row = 4, column = 5)

root = Tk()



root_specs(root)
root_widgets(root)


root.mainloop()