#lista de tarefas
def main():
    tarefas = []

#adicionar
    while True:
        print("\n--- Menu de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)

        elif opcao == "2":
            if tarefas:
               for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("Não possui tarefas")
            
        elif opcao == "3":
            for i, tarefa in enumerate(tarefas, 1):
                 print(f"{i}. {tarefa}")
            try:     
                texto = input("Qual numero do item para remoção? ")
                numero = int(texto)
                indice = numero -1
                tarefas.pop(indice)
            except:
                print("Entrada inválida ou número inexistente.")

        elif opcao == "4":
            break
main()