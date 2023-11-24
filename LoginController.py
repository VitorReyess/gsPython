from Usuario import Usuario  # Importa a classe Usuario de um módulo chamado Usuario
from MenuSystem import MenuSystem  # Importa a classe MenuSystem de um módulo chamado MenuSystem
import json # Importa o json

class LoginController:
    def __init__(self):
        self.users = self.loadUsers()  # Inicializa uma lista vazia para armazenar usuários

    def loadUsers(self):
        try:
            with open("sistemaReal/users.json", "r") as jsonFile:
                usersData = json.load(jsonFile)  # Lê os dados de usuários de um arquivo JSON
                userObjects = []
                try:
                    for user_data in usersData:
                        userObjects.append(Usuario(user_data['login'],user_data['senha']))  # Cria objetos de usuário com base nos dados lidos
                    return userObjects  # Retorna a lista de objetos de usuário
                except:
                    print("Não foi possível criar usuários")
                    print(userObjects)
            return []
        except:
            print("404 - Arquivo JSON não encontrado")
            return []

    def login(self):
        # Solicita ao usuário o nome de usuário e senha
        login = input('Usuario: ')
        senha = input('Senha: ')

        # Itera sobre a lista de usuários
        for usuario in self.users:
            # Verifica se há uma correspondência de nome de usuário e senha
            if usuario.login == login and usuario.password == senha:
                print('Login com sucesso!\n')  # Exibe uma mensagem de login bem-sucedido
                self.menuSystem = MenuSystem()  # Cria uma instância da classe MenuSystem
                return self.menuSystem.menuOption()  # Chama o método menuOption de MenuSystem

        # Se nenhum usuário correspondente for encontrado, exibe uma mensagem de erro
        else:
            print('\nUsuário ou senha incorretos\n')

    def register(self):
        print(20 * '-')
        print("\nCADASTRO DE USUÁRIO")
        print(20 * '-')
        
        # Solicita ao usuário um nome de usuário e senha
        login = input("Digite seu login de usuário: ")
        senha = input("Digite sua senha de usuário: ")
        
        # Cria uma instância da classe Usuario com o nome de usuário e senha fornecidos
        self.users.append(Usuario(login, senha))  # Adiciona um novo objeto de usuário à lista de usuários
        
        return print("Usuário cadastrado!")  # Exibe uma mensagem indicando que o usuário foi cadastrado
