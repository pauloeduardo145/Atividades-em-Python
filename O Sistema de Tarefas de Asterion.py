tarefas = []
def main():
    
    lerar()

    
    while True:
        print("Os fragmentos persistem apenas enquanto forem preservados.")
        print("\n--- Menu de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
            salvar_arquivo()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            remover_tarefa()
            salvar_arquivo()

        elif opcao == "4":
            salvar_arquivo()
            break

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)

def listar_tarefas():
    if tarefas:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Não possui tarefas")

def remover_tarefa():
    for i, tarefa in enumerate(tarefas, 1):
                 print(f"{i}. {tarefa}")
    try:     
        texto = input("Qual numero do item para remoção? ")
        numero = int(texto)
        indice = numero -1
        tarefas.pop(indice)
    except:
        print("Entrada inválida ou número inexistente.")
    
def salvar_arquivo():

    with open('lista.txt', 'w', encoding='utf-8') as arquivo:
        for item in tarefas:
            arquivo.write(f'{item}\n')

def lerar():
    try:
        with open('lista.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                if tarefa:
                    tarefas.append(tarefa)
            print("Tarefas carregadas com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de tarefas encontrado. Começando com a lista vazia.")

main()
