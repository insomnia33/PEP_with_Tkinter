from tkinter import *
from functools import partial

def root_specs(janela): #Propriedades da janela principal
	lb = Label(janela, bg = "black")
	lb.grid(row = 1, column = 1)
	janela.title("Prontuário Eletrônico de Pacientes")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("350x150+100+100")

def cadastro_medico_specs(janela): #Propriedades da janela de Cadastro Medico
	
	janela.title("Cadastro do Médico")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("280x150+200+200")

def cadastro_pacientes_specs(janela): #Propriedades da janela de Cadastro do Paciente
	
	janela.title("Cadastro do Paciente")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("280x150+200+200")

def cadastro_anamnese_specs(janela): #Propriedades da janela de Cadastro da Anamnese
	
	janela.title("Cadastro da Anamnese")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("280x150+200+200")

def pesquisar_medico_specs(janela): #Propriedades da janela de Pesquisar Medico
	
	janela.title("Pesquisar Médico")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("200x200+100+100")

def pesquisar_paciente_specs(janela): #Propriedades da janela de Pesquisar Paciente
	
	janela.title("Pesquisar Paciente")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("200x200+100+100")

def pesquisar_anamnese_specs(janela): #Propriedades da janela de Pesquisar Anamnese
	
	janela.title("Pesquisar Anamnese")
	janela["background"] = "black"
	#Largura x Altura + DistEsquerda + DistTopo
	janela.geometry("200x200+100+100")



def cadastro_medico(): # Janela de Cadastro Medico
	janela = Tk()
	cadastro_medico_specs(janela) 
	

	global nomemed
	global crm
	global especialidade
	global medid

	lbnome = Label(janela, fg="Green", bg="black", text="Nome: ")
	nomemed = Entry(janela, fg="GREEN", bg="Black")
	lbcrm = Label(janela, fg="Green", bg="black", text="CRM: ")
	crm = Entry(janela, fg="GREEN", bg = "black")
	lbespecialidade = Label(janela, fg="green", bg = "black", text="Esp: ")
	especialidade = Entry(janela, fg="green", bg="black")
	lbmedid = Label(janela, fg="green", bg = "black", text="ID: ")
	medid = Entry(janela, fg="green", bg="black")

	lbnome.grid(row = 1, column = 1)
	nomemed.grid(row = 1, column = 2)
	
	lbcrm.grid(row = 2, column = 1)
	crm.grid(row = 2, column = 2)

	lbespecialidade.grid(row = 3, column = 1)
	especialidade.grid(row = 3, column = 2)

	lbmedid.grid(row = 4, column = 1)
	medid.grid(row = 4, column = 2)

	btsave = Button(janela, bg="black", fg="green", text = "SALVAR")
	btsave.grid(row = 5, column = 2)

	janela.mainloop()

def cadastro_paciente(): # Janela de Cadastro de Pacientes
	janela = Tk()
	cadastro_pacientes_specs(janela)

	global nomepac
	global cpf
	global rg
	global sexo

	lbnome = Label(janela, fg="Green", bg="black", text="Nome: ")
	nomepac = Entry(janela, fg="GREEN", bg="Black")
	lbcpf = Label(janela, fg="Green", bg="black", text="CPF: ")
	cpf = Entry(janela, fg="GREEN", bg = "black")
	lbrg = Label(janela, fg="green", bg = "black", text="RG: ")
	rg = Entry(janela, fg="green", bg="black")
	lbsexo = Label(janela, fg="green", bg = "black", text="Sexo: ")
	sexo = Entry(janela, fg="green", bg="black")

	lbnome.grid(row = 1, column = 1)
	nomepac.grid(row = 1, column = 2)
	
	lbcpf.grid(row = 2, column = 1)
	cpf.grid(row = 2, column = 2)

	lbrg.grid(row = 3, column = 1)
	rg.grid(row = 3, column = 2)

	lbsexo.grid(row = 4, column = 1)
	sexo.grid(row = 4, column = 2)

	btsave = Button(janela, bg="black", fg="green", text = "SALVAR")
	btsave.grid(row = 5, column = 2)

	janela.mainloop()

def cadastro_anamnese(): # Janela de Cadastro de Anamnese
	janela = Tk()
	cadastro_anamnese_specs(janela)
	janela.mainloop()

def pesquisar_medico(): # Janela para Pesquisar Medicos
	janela = Tk()
	pesquisar_medico_specs(janela)
	janela.mainloop()

def pesquisar_paciente(): # Janela para Pesquisar Pacientes
	janela = Tk()
	pesquisar_paciente_specs(janela)
	janela.mainloop()

def pesquisar_anamnese(): # Janela para Pesquisar Anamnese
	janela = Tk()
	pesquisar_anamnese_specs(janela)
	janela.mainloop()



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