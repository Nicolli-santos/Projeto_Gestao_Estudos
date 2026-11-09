import json

ARQUIVO = "dados_estudos.json"

materias = []
tarefas = []

# Carregar dados salvos
try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        if isinstance(dados, list):
            materias = dados
            tarefas = []
        else:
            materias = dados.get("materias", [])
            tarefas = dados.get("tarefas", [])

except FileNotFoundError:
    materias = []
    tarefas = []


while True:
    print()
    print("================================")
    print("       SISTEMA DE ESTUDOS")
    print("================================")
    print("1 - Cadastrar matéria")
    print("2 - Listar matérias")
    print("3 - Registrar nota")
    print("4 - Ver média")
    print("5 - Adicionar tarefa")
    print("6 - Listar tarefas")
    print("7 - Concluir tarefa")
    print("8 - Salvar dados")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar matéria
    if opcao == "1":
        nome_materia = input("Digite o nome da matéria: ")

        materias.append({
            "nome": nome_materia,
            "notas": []
        })

        print("Matéria cadastrada:", nome_materia)

    # Listar matérias
    elif opcao == "2":
        print()
        print("Matérias cadastradas:")

        if len(materias) == 0:
            print("Nenhuma matéria cadastrada.")
        else:
            for materia in materias:
                print("-", materia["nome"])

    # Registrar nota
    elif opcao == "3":
        print()
        print("Matérias cadastradas:")

        if len(materias) == 0:
            print("Nenhuma matéria cadastrada.")
        else:
            for i, materia in enumerate(materias):
                print(i + 1, "-", materia["nome"])

            escolha = int(input("Escolha o número da matéria: "))

            if escolha >= 1 and escolha <= len(materias):
                nota = float(input("Digite a nota: "))

                materias[escolha - 1]["notas"].append(nota)

                print("Nota registrada com sucesso!")
            else:
                print("Matéria inválida.")

    # Ver média
    elif opcao == "4":
        print()
        print("Matérias cadastradas:")

        if len(materias) == 0:
            print("Nenhuma matéria cadastrada.")
        else:
            for i, materia in enumerate(materias):
                print(i + 1, "-", materia["nome"])

            escolha = int(input("Escolha o número da matéria: "))

            if escolha >= 1 and escolha <= len(materias):
                materia = materias[escolha - 1]

                if len(materia["notas"]) == 0:
                    print("Essa matéria ainda não possui notas.")
                else:
                    soma = sum(materia["notas"])
                    media = soma / len(materia["notas"])

                    print("Notas:", materia["notas"])
                    print("Média:", media)
            else:
                print("Matéria inválida.")

    # Adicionar tarefa
    elif opcao == "5":
        descricao = input("Digite a tarefa: ")

        tarefas.append({
            "descricao": descricao,
            "concluida": False
        })

        print("Tarefa adicionada com sucesso!")

    # Listar tarefas
    elif opcao == "6":
        print()
        print("Tarefas:")

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                if tarefa["concluida"]:
                    status = "Concluída"
                else:
                    status = "Pendente"

                print(i + 1, "-", tarefa["descricao"], "-", status)

    # Concluir tarefa
    elif opcao == "7":
        print()
        print("Tarefas:")

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                if tarefa["concluida"]:
                    status = "Concluída"
                else:
                    status = "Pendente"

                print(i + 1, "-", tarefa["descricao"], "-", status)

            escolha = int(input("Escolha o número da tarefa: "))

            if escolha >= 1 and escolha <= len(tarefas):
                tarefas[escolha - 1]["concluida"] = True
                print("Tarefa concluída com sucesso!")
            else:
                print("Tarefa inválida.")

    # Salvar dados
    elif opcao == "8":
        dados = {
            "materias": materias,
            "tarefas": tarefas
        }

        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

        print("Dados salvos com sucesso.")

    # Sair
    elif opcao == "9":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 9.")