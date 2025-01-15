import datetime as d
import json as j


def adiciona_tarefa():
    
    data_cadastro = d.date.today()
    data_cadastro_str =  data_cadastro.strftime("%d-%m-%Y")

    entrada_id = input("Digite o ID da tarefa: ")
    entrada_titulo = input("Escreva o título da tarefa: ")
    entrada_descricao = input("Escreva a descrição da tarefa: ")
    entrada_data_cadastro = data_cadastro_str

    tarefa = {
        "id": entrada_id,
        "titulo": entrada_titulo,
        "descricao": entrada_descricao,
        "data_cadastro": entrada_data_cadastro,
        "concluida": False
    }

    with open("db_tarefas.json", "w") as db_tarefas:
        j.dump(tarefa, db_tarefas)

adiciona_tarefa()

with open("db_tarefas.json", "r") as leitura:  
    conteudo = leitura.read()
    print(conteudo)


   