#Kened Wanderson Cruz Oliveira
#Engenharia de Computação - UFPB

# PORTA OR(ou)
# [0,0] | 0
# [0,1] | 1
# [1,0] | 1
# [1,1] | 1

#PORTA AND(e)
# [0,0] | 0
# [0,1] | 0
# [1,0] | 0
# [1,1] | 1


# maximo de interacoes
max_int = 20

# entradas
x = [[0,0], [0,1], [1,0], [1,1]]

# quantos itens tem o vetor x (4)
tamanho_x = len(x)

# quantos itens estão em cada posicao do vetor x
qtde_itens_x = len(x[0])


# taxa de aprendizado
taxa_aprendizado = 0.5

#Resposta desejada
while 1:

    saida = 0
    resposta = ""
    somatorio = 0
    erro = 0

    # pesos
    w = [0,0]

    # quantos itens tem o vetor w (2)
    tamanho_w = len(w)


    escolha = raw_input("Qual Porta você deseja? OU/E/sair ")
    if (escolha == "E" or escolha == "e"):
        d = [0,0,0,1]#AND
        
    elif (escolha == "OU" or escolha == "ou"):
        d = [0,1,1,1]#OR
        
    elif (escolha == "sair"):
        break

    print("Treinando")

    # inicio
    for k in range(1,max_int):
        acertos = 0    
        erro = 0
        print("INTERACAO "+str(k)+"-------------------------")
        for t in range(0,tamanho_x):        
            somatorio = 0

            # para calcular a saida,cada x é multiplicada pelo seu peso w correspondente
            for j in range(0,qtde_itens_x):
                somatorio += x[t][j] * w[j]

            # funcao de saida
            if somatorio > 0.5:
                saida = 1       
            else:
                saida = 0

            # atualiza os pesos caso a saida seja errada        
            if saida == d[t]:
                resposta = "acerto"
                acertos += 1
                erro = 0            
            else:
                resposta = "erro  "        
                # calculando o erro
                erro = d[t] - saida 
                # atualizando os pesos            
                for j in range (0,tamanho_w):
                    w[j] = w[j] + (taxa_aprendizado * erro * x[t][j])        

            print(resposta + " >>> soma = "+str(somatorio)+ ", saida = "+ str(saida)+ ", erro = "+str(erro))

        if acertos == tamanho_x:
            print("\nFuncionalidade aprendida com "+str(k)+" interacoes")
            print("\nPesos encontrados")
            for j in range (0,tamanho_w):
                print(w[j])
            break;
        print("")
