import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    try:
        with open(path_file, "r") as file:
            content = file.read()
            return content.split("\n")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None


print(txt_importer("statics/arquivo_teste.txt"))
