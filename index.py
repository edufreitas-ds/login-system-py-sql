# Importa as Bibliotecas
from tkinter import *
from tkinter import messagebox # Mensagem para Usuario
from tkinter import ttk
import DataBaser

# Criar nossa janela
janela = Tk()
janela.title("Sistemas DP - Painel de Acesso")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False) # Não permite ampliar ou reduzir a largura e altura da janela.
janela.attributes("-alpha", 0.9) # Transparência
janela.iconbitmap(default="icons/LogoIcon.ico") # Carrega o ícone

# Carregando Images
logo = PhotoImage(file="icons/logo.png")

#================ CRIANDO WIDGETS ================

# Separar a Janela em duas partes: Esquerda e Direita
LeftFrame = Frame(janela, width=200, height=300, bg="#122620", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=390, height=300, bg="#122620", relief="raise")
RightFrame.pack(side=RIGHT)

# Trazendo a Logo
LogoLabel = Label(LeftFrame, image=logo, bg="#122620")
LogoLabel.place(x=50, y=100)

# Criando o Usuario com Entrada de Dados
UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="#122620", fg="White")
UserLabel.place(x=50, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=160, y=113)

# Criando a Senha com Entrada de Dados
PasswordLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="#122620", fg="White")
PasswordLabel.place(x=62, y=140)

PasswordEntry = ttk.Entry(RightFrame, width=30, show="●")
PasswordEntry.place(x=160, y=153)

# Define uma função que realiza o Login utilizando User e Password que devem estar registrados no Banco de Dados.
def Login():
    User = UserEntry.get()
    Password = PasswordEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Password))
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Password in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado!")
    except:
        messagebox.showerror(title="Login Info", message="Acesso negado. Login ou Senha não registradas no sistema.")

#================ CRIANDO BOTÕES ================

# Criando botão de Login
LoginButton = ttk.Button(RightFrame, text="Entrar", width=29, command=Login)
LoginButton.place(x=160, y=193)

# Define uma função que registra o usuário.
def Register():
    # Removendo os Widgets de Login da Tela
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # Inserindo Widgets de Cadastro
    # Criando o campo Nome com Entrada de Dados
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="#122620", fg="White")
    NomeLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=40)
    NameEntry.place(x=104, y=20)

    # Criando o campo E-mail com Entrada de Dados
    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20), bg="#122620", fg="White")
    EmailLabel.place(x=10, y=40)

    EmailEntry = ttk.Entry(RightFrame, width=40)
    EmailEntry.place(x=104, y=55)

    # Define a função que registra os a conta no banco de dados.
    def RegisterToDatabase():

        # Pega nome, e-mail, usuario e senha escritos nos campos...
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PasswordEntry.get()

        # Se tiver um campo vazio, retorna um erro...
        if not Name  or not Email or not User or not Password:
            messagebox.showerror(title="Register Error", message="Preencha todos os campos.")

        # Se não, insere os dados na base de dados.
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password)
            VALUES (?, ?, ?, ?)
            """,(Name, Email, User, Password))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message= "Conta criada com sucesso.")

    # Criando botão para registrar o cadastro.
    Register = ttk.Button(RightFrame, text="Registrar", width=29, command=RegisterToDatabase)
    Register.place(x=160, y=193)

    # Define função que retorna para janela de Login.
    def BackToLogin():
        # Removendo Widgets do Cadastro
        NomeLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # Trazendo de volta os Widgets de Login
        RegisterButton.place(x=200, y=233)
        LoginButton.place(x=160, y=193)

    # Criando botão que volta para a janela de login.
    Back = ttk.Button(RightFrame, text="Voltar", width=15, command=BackToLogin)
    Back.place(x=200, y=233)

# Criando botão para iniciar o cadastro.
RegisterButton = ttk.Button(RightFrame, text="Cadastrar", width=15, command=Register)
RegisterButton.place(x=200, y=233)


janela.mainloop() # Propriedades da nossa janela encerrou

