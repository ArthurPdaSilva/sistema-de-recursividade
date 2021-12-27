import metodos

resposta = 0
menu = '''
1 - Saber o tamanho de uma string
2 - Somar uma string composta por números
3 - Saber quantas vezes uma string apareceu numa string
4 - Exponenciação ou multiplicação de dois valores
5 - Multiplicar ou soma os elementos de uma lista
6 - Descobrir o maior e o menor elemento de uma lista
7 - Converter decimal para binário
8 - Converter binário para decimal
9 - Fibonacci
10 - Ver novamente o menu
11 - Sair
'''

print(menu)
while(resposta != 11):
    resposta = int(input("Escolha uma opção (ver o menu é 10): "))
    if(resposta == 1 or resposta == 2):
        palavra = input("Digite uma frase: ")
        if(resposta == 1):
            print(f"O tamanho da string é: {metodos.tamanhoString(palavra)}")
        else:
            letra = input("Qual letra você quer procurar? ")[0]
        print(f"A quantidade de vezes que a letra {letra} apareceu na palavra {palavra} foi: {metodos.letraString(palavra, letra)}")
    elif(resposta == 2):
        palavra = input("Digite uma frase composto por números ex: (11112): ")
        print(f"A soma de {palavra} é: {metodos.somarStringInt(palavra)}")      
    elif(resposta == 4):
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        opcao = input("Deseja fazer (1) multiplicação ou (2) exponenciação recursiva: ")
        if(opcao == 1):
            print(f"{n1} X {n2} é: {metodos.multi(n1, n2)}")
        elif(opcao == 2):
            print(f"{n1} elevado a {n2} é: {metodos.expo(n1,n2)}")
        else:
            print("Opção inválida!")
    elif(resposta == 5 or resposta == 6):
        lista = []
        listaT = int(input("Qual é o tamanho da lista? "))
        for i in range(listaT):
            x = int(input("Digite um número: "))
            lista.append(x)
        if(resposta == 5):
            print(f'''A lista {lista}, a multiplicação de seus valores é {metodos.listaMulti(lista)}
            e a soma dos elementos é: {metodos.listaSoma(lista)}''')
        else:
            opc = int(input("Deseja saber (1) o maior valor da lista ou (2) o menor valor da lista: "))
            if(opc == 1):
                print(f"O maior valor da lista é: {metodos.maiorV(lista)}")
            elif(opc == 2):
                print(f"O menor valor da lista é: {metodos.menorV(lista)}")
            else:
                print("Opção inválida!")
    elif(resposta == 7):
        n1 = int(input("Digite número decimal: "))
        print(f"O número {n1} em binário é: {metodos.binarioValor(n1)}")
    elif(resposta == 8):
        n1 = input("Digite número em binário: ")
        print(f"O número {n1} em decimal é: {metodos.decimalValor(n1)}")
    elif(resposta == 9):
        termo = int(input("Qual termo? "))
        print(f"O termo {termo} é o: {metodos.fibo(termo)}")
    elif(resposta == 10):
        print(menu)
    elif(resposta == 11):
        print("Saindo do programa...")
    else:
        print("Opção inválida, veja o menu novamente (10)!")

print("Programa finalizado")
