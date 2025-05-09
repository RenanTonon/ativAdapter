import csv
from Pessoa import Pessoa
class PessoaCsvAdapter:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def listar_pessoas(self):
        pessoas = []
        try:
            with open(self.caminho_arquivo, mode='r', encoding='utf-8') as file:
                leitor_csv = csv.reader(file)
                next(leitor_csv) 
                for linha in leitor_csv:
                    if len(linha) == 3:
                        nome = linha[0].strip()
                        idade = int(linha[1].strip())
                        email = linha[2].strip()
                        pessoa = Pessoa(nome, idade, email)
                        pessoas.append(pessoa)
                    else:
                        print(f"Formato inválido na linha: {linha}")

        except FileNotFoundError:
            print(f"Erro: O arquivo {self.caminho_arquivo} não foi encontrado.")
        except ValueError as e:
            print(f"Erro ao converter idade ou outro valor: {e}")

        return pessoas
