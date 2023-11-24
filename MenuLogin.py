from LoginController import LoginController  # Importa a classe LoginController de um módulo chamado LoginController

class MenuLogin:
    def __init__(self):
        print(20 * '-')
        print('MENU LOGIN')
        print(20 * '-')
        self.mainMenuOption = 0  # Inicializa uma variável chamada mainMenuOption com o valor 0
        self.loginController = LoginController()  # Cria uma instância da classe LoginController

    def menuOption(self):
        while self.mainMenuOption != '3':  # Executa o loop até que a opção do menu seja '3'
            mainMenuOption = input("1 - Login\n2 - Criar conta\n3 - Sair\n\nDigite a opção selecionada: ")
            if mainMenuOption == '1':
                self.loginController.login()  # Chama o método login da instância de LoginController
            elif mainMenuOption == '2':
                self.loginController.register()  # Chama o método register da instância de LoginController
            elif mainMenuOption == '3':
                print("Finalizando programa!")  # Exibe uma mensagem de despedida
                break  # Sai do loop e finaliza o programa
