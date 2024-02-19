from queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    lines = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    if instance.index_of(new_dict) == -1:
        instance.enqueue(new_dict)
        print(new_dict)
    else:
        print("Arquivo já importado")


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        instance.dequeue()
        print(f"Arquivo {instance} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    queue = Queue()
    process("statics/arquivo_teste.txt", queue)
