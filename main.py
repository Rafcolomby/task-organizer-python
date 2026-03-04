import json
import os
ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists (ARQUIVO):
        return[]
      with open(ARQUIVO, "r") as f:
        return json.load(f)

  def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
      json.dump(tarefas, f, indent=4)

def adicionar_tarefas(tarefas):
  tarefa = input("Digite a nova tarefa: ")
  tarefas.append({"tarefa": tarefa, "concluida": False})
  salvar_tarefas(tarefas)
  print("Tarefa adicionada!")

def listar_tarefas(tarefas)
  if not tarefas:
    print("Nenhuma tarefa cadastrada.")
    return
  for i, t in enumerate(tarefas):
    status = "[ok]" if t ["concluida] else "[ ]"
    print (f"{i+1}. [{status}] {t{'tarefa']}")

def concluir_tarefa(tarefas)
  listar_tarefas(tarefas)
  num = int (input("Número da tarefa para concluir: ") )
  tarefas[num-1]["concluida"] = True
  salvar_tarefas(tarefas)
  print("Tarefa concluída!")

def menu():
  tarefas = carregar_tarefas()

  while True:
    print("\n=== ORGANIZADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha: ")
    if opcao == "1":
     listar_tarefas(tarefas)
    elif opcao == "2":
      adicionar_tarefa(tarefas)
    elif opcao == "3":
      concluir_tarefa(tarefas)
    elif opcap == "4":
      break 
    else:
      print("Opção inválida")

menu()
