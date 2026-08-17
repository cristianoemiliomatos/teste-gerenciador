from cruds.rh import rh
from cruds.adm import adm
from cruds.clientes import cliente


print("|========================|")
print("|SISTEMA DE GERENCIAMENTO|")
print("|========================|")

print("\n")
print("1 - Sistema do ADM")
print("2 - Sistema do RH")
print("3 - Sistema do Cliente")

opcao = int(input("Digite a opção que você deseja: "))

match opcao:
    case 1:
        adm()
    case 2:
        rh()
    case 3:
        cliente()