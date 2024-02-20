from ting_file_management.queue import Queue

from ting_file_management.file_process import process


def exists_word(word, instance):

    report = []
    for file in instance.queue():
        ocorrencias = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1})
                # print(f"Arquivo: {file['nome_do_arquivo']}, Linha: {index + 1}, Ocorrências: {ocorrencias}")
            else:
                print("nao encontrado")
            # print(ocorrencias)
        if len(ocorrencias) > 0:
            report.append({"palavra": word, "arquivo": file["nome_do_arquivo"], "ocorrencias": ocorrencias})
    return report


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    queue = Queue()
    process("statics/arquivo_teste.txt", queue)
    print(exists_word("de", queue))
    # search_by_word("teste", queue)
