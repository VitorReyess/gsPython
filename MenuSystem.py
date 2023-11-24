from consulta import   # Importa a classe EnergyStorage de um módulo chamado EnergyStorage
from quiz import psychological  # Importa a classe CalculoConsumo de um módulo chamado CalculoConsumo

class MenuSystem:
    def __init__(self):
       
        print(20 * '-')
        print('MENU DIAGNOSTICO')
        print(20 * '-')
        self.mainMenuOption = 0
        
    def menuOption(self):
        while self.mainMenuOption != '3': 
            mainMenuOption = input("1 - Quiz\n2 - consultar diagnostico\n3 - Log out \nDigite a opção selecionada: ")
            if mainMenuOption == '1':
                
                self. = ()
                self..()
            elif mainMenuOption == '2':
                
                self. = ()
                self..()
                
            elif mainMenuOption == '3':
                print("Fazendo logout!")  # Exibe uma mensagem de despedida
                break  # Sai do loop e finaliza o programa

        