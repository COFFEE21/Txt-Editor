import os
from os import write


class File:

    file_path = "/home/coffee/PycharmProjects/PythonProject/Txt-Editor/Default_Local/Output.txt"
    txt_data = "Eu quero escrever alguma coisa aqui"

    def __init__(self,path = "/home/coffee/PycharmProjects/PythonProject/Txt-Editor/Default_Local/Output.txt"):
       self.path = path

       with open(path , "w") as file:
           write("")


    @staticmethod
    def check(path):

         if os.path.isfile(path):
            print("É um camihno válido para um arquivo")

         elif os.path.isdir(path):
            print("É um caminho válido para um diretório")

         else:
            print("Não é um caminho válido")

    def escrever(self):
        path = self.path
        data = f"\n{input("O que você deseja escrever no arquivo?")}"
        with open(path, mode ="a") as file:
            file.write(data)
            print("escrita do arquivo realizada")

    def ler(self):
      path = self.path
      try:
        with open(path, "r") as file:
            content = file.read()
            return content

      except FileNotFoundError:
        print("Arquivo não encontrado!")

    def resetar(self):
        path = self.path
        with open(path ,"w") as file:
            file.write("")






