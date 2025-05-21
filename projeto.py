# lista de filmes
filmes=[]

#funcao para adaptaçao de titulo
def padronizar_titulo(titulo):
    return titulo.strip().title()

# função para classificar o filme com base na nota
def classificar_nota(nota):
    if nota >= 8:
        return "Bom"
    elif nota>= 5:
        return "Regular"
    else:
        return"Ruim"
   
# funcao de cadastrar filme
def cadastra_filme():
    titulo=padronizar_titulo(input("Título do filme:"))
    try:
        ano = int(input("Ano do lançamento:"))
        nota = float(input("Nota (0 a 10):"))
        if nota < 0 or nota > 10:
            raise ValueError("nota fora do intervalo.")
    except ValueError as e:
        print("Entrada inválida",e)
        return
    genero = input("Gênero:").strip().title()
    filmes.append({'titulo': titulo, 'ano': ano, 'genero': genero, 'nota': nota})

#funcao de listar os filmes
def listar_filmes():
    for filme in filmes:
        print(f"{filme['titulo']} ({filme['ano']}) ({filme['genero']}) ({filme['nota']}) Classificação:{classificar_nota(filme['nota'])}")

#funcao para busca de filme por nome
def buscar_filmes():
    for filme in filmes:
        busca= padronizar_titulo(input("Digite o títilo do filme desejado:"))
        for filme in filmes:
                if filme == busca:
                    print(f"Filme encontrado: {filme}")
                    return
                else:
                    print("Filme não encontrado.")

#funcao de remover filme por nome
def remover_filme():
     titulo=padronizar_titulo(input("Título do filme a remover:"))
     for filme in filmes:
         if filme == titulo:
             filmes.remove(filme)
             print("Filme removido com sucesso!")
             return
         else:
             print("Filme nao encontrado!")

# funcao de exibir estatisticas
def exibir_estatisticas():
    if not filmes:
        print("Nenhum filme cadastrado")
        return
    print(f"Quantidade de filmes:{len(filmes)}")
    media = sum(f['nota']for f in filmes)/len(filmes)
    print(f"Média das notas:{media:2f}")

#funcao para mostrar os generos mais cadastrados
generos = {}
for f in filmes:
    generos[f['genero']]= generos.get(f['genero'],0) + 1
    genero_mais= max(generos,key=generos.get)
    print(f"Gênero mais cadastro:{genero_mais} ")

#filmes com nota >=8
print("Filmes com nota >=8:")
for f in filmes:
    if f['nota'] >= 8:
        print(f" -{f['titulo']} ({f['nota']})")

#menu
def menu():
    while True:
        print("\n---Menu principal---")
        print("1- Cadastrar Filme")
        print("2- Listar Filmes")
        print("3- Buscar Filme por nome ")
        print("4- Remover Filme por nome ")
        print("5- Exibir estatísticas")
        print("6- sair")
        opcao= input("Escolha uma opção")


        if opcao =='1':
            cadastra_filme()
        elif opcao =='2':
            listar_filmes()
        elif opcao =='3':
            buscar_filmes()
        elif opcao =='4':
            remover_filme()
        elif opcao =='5':
            exibir_estatisticas()
        elif opcao == '6':
            print('Encerrando o programa')
            break
menu()






