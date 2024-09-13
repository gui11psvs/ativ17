# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input("Digite um ano: "))
if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")