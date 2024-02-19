import sys


def txt_importer(path_file):
    try:
        if not path_file.lower().endswith(".txt"):
            print("Formato inválido", file=sys.stderr)

        with open(path_file, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


if __name__ == "__main__":
    print(txt_importer("statics/arquivo_teste.txt"))
