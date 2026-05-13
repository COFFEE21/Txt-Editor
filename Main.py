import os

file_path = "/home/coffee/PycharmProjects/PythonProject/Txt-Editor/Data.txt"
txt_data = "Eu quero escrever alguma coisa aqui"

def check(path):

    if os.path.isfile(path):
        print("É um camihno válido para um arquivo")

    elif os.path.isdir(path):
        print("É um caminho válido para um diretório")

    else:
        print("Não é um caminho válido")

def escrever(path):
    with open(path, mode ="w") as file:
        file.write(txt_data)
        print("escrita do arquivo realizada")

def ler(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print("Arquivo não encontrado!")




escrever(file_path)
