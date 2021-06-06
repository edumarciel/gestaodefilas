import os 
from time import sleep 
import datetime 
import time 

#DATA E HORA 
hora = time.localtime()
data = datetime.datetime.now()

#LISTA PARA SENHAS
convencional = []
preferencial = []


#MENU OPCIONAL
def Menu():
    print("======================================================================\n")
    print("|                   INFORME O TIPO DE ATENDIMENTO                    |\n")
    print("|____________________________________________________________________|\n")
    print("|            1 - Convencional       |   2 - Preferencial             |\n")
    print("|____________________________________________________________________|\n")
    
    global opcao
    opcao = int(input("Informe a operação desejada\n"))
    os.system("cls")
    if opcao == 1:
        Convencional()
    elif opcao == 2:
        Preferencial()
    else:
        print("\033[31mOpção invalida. Tente Novamente !\033[m")
        sleep(2)
        os.system("cls")
    Menu()

#MENU CONVENCIONAL
def Convencional():
    print("======================================================================\n")
    print("|                    ATENDIMENTO CONVENCIONAL                        |\n")
    print("|____________________________________________________________________|\n")
    print("|            1 - Caixa       |   2 - Guichê                          |\n")
    print("|____________________________________________________________________|\n")
    print("|            3 - Gerência    |   4- Acompanhamento                   |\n")
    print("|____________________________________________________________________|\n")
    

    global opcao
    opcao = int(input("Informe o setor para o atendimento \n"))
    if opcao == 1:
        convencional.append("CXC" + str(len(convencional)+1))
        os.system("cls")
        ImprimirConvencional()
    
    elif opcao == 2:
        convencional.append("GHC" + str(len(convencional)+1))
        os.system("cls")
        ImprimirConvencional()

    elif opcao == 3:
        convencional.append("GEC" + str(len(convencional)+1))
        os.system("cls")
        ImprimirConvencional()

    elif opcao == 4:
        ()

    else:
        print("\033[31mOpção invalida. Tente Novamente !\033[m")
        sleep(2)
        os.system("cls")
    Menu()

#MENU PREFERENCIAL
def Preferencial():
    print("======================================================================\n")
    print("|                    ATENDIMENTO PREFERENCIAL                        |\n")
    print("|____________________________________________________________________|\n")
    print("|            1 - Caixa       |   2 - Guichê                          |\n")
    print("|____________________________________________________________________|\n")
    print("|            3 - Gerência    |   4- Acompanhamento                   |\n")
    print("|____________________________________________________________________|\n")

    global opcao
    opcao = int(input("Informe o setor para o atendimento \n"))
    if opcao == 1:
        preferencial.append("CXP" + str(len(preferencial)+1))
        os.system("cls")
        ImprimirPreferencial()

    elif opcao == 2:
        preferencial.append("GHP" + str(len(preferencial)+1))
        os.system("cls")
        ImprimirPreferencial()

    elif opcao == 3:
        preferencial.append("GEP" + str(len(preferencial)+1))
        os.system("cls")
        ImprimirPreferencial()

    elif opcao == 4:
        ()

    else:
        print("\033[31mOpção invalida. Tente Novamente !\033[m")
        sleep(2)
        os.system("cls")
    Menu()

#FUNÇÃO IMPRIMIR SENHA CONVENCIONAL
def ImprimirConvencional():
        print("=================================================================\n")
        print("                SISTEMA DE GESTÃO DE FILAS                      \n")
        print("=================================================================\n")
        print("                 BANCO NOSSO CRÉDITO                            \n")
        print("                 Av. Principal Nº 100, Centro                   \n")
        print("                 Fone (86)96115-1568                            \n")
        print("=================================================================\n")
        print("                 SENHA: " + str(convencional[-1]))
        print("                 Tipo: Convencional")
        print("                 Data: " +str(data.day) + "/" + str(data.month) + "/" + str(data.year))
        print("                 Hora: " +str(hora[3])  + ":" + str(hora[4])    + " horas" )
        print("=================================================================\n")
        sleep(2)
        os.system("cls") 

#FUNÇÃO IMPRIMIR SENHA PREFERENCIAL
def ImprimirPreferencial():
        print("=================================================================\n")
        print("                SISTEMA DE GESTÃO DE FILAS                      \n")
        print("=================================================================\n")
        print("                 BANCO NOSSO CRÉDITO                            \n")
        print("                 Av. Principal Nº 100, Centro                   \n")
        print("                 Fone (86)96115-1568                            \n")
        print("=================================================================\n")
        print("                 SENHA: " + str(preferencial[-1]))
        print("                 Tipo: Preferencial")
        print("                 Data: " +str(data.day) + "/" + str(data.month) + "/" + str(data.year))
        print("                 Hora: " +str(hora[3])  + ":" + str(hora[4])    + " horas" )
        print("=================================================================\n")
        sleep(2)
        os.system("cls")

#PAINEL DE CONTROLE


#FIM DO PROGRAMA            
opcao=1
while(opcao<3):
    Menu()
