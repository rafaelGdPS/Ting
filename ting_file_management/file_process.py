import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt_list = txt_importer(path_file)

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_list),
        "linhas_do_arquivo": txt_list,
    }
    if instance.__len__() == 0:
        instance.enqueue(file)
        print(file, file=sys.stdout)
        return None

    for path in instance._data:
        if path["nome_do_arquivo"] == path_file:
            return None

        instance.enqueue(file)
        print(file, file=sys.stdout)
        return None


def remove(instance):
    if instance.__len__() == 0:
        print("Não há elementos")
        return
    path = instance.dequeue()["nome_do_arquivo"]

    print(f"Arquivo {path} removido com sucesso")
    return


def file_metadata(instance, position):
    instance_size = instance.__len__() - 1
    if (
        not isinstance(position, int)
        or position < 0
        or position > instance_size
    ):
        print("Posição inválida", file=sys.stderr)
        return
    instance_at = instance.search(position)
    print(instance_at)
