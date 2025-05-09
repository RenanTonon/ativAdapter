from PessoaCsvAdapter import PessoaCsvAdapter

def main():
    caminho_csv = 'listadepessoas.csv'
    adaptador = PessoaCsvAdapter(caminho_csv)
    pessoas = adaptador.listar_pessoas()

    for pessoa in pessoas:
        print(pessoa)

if __name__ == '__main__':
    main()
