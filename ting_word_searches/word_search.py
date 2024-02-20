from ting_file_management.queue import Queue

from ting_file_management.file_process import process


def search_word_in_file(word, file):
    occurrences = []
    for index, line in enumerate(file["linhas_do_arquivo"], start=1):
        if word.lower() in line.lower():
            occurrences.append({"linha": index, "conteudo": line})
    return occurrences


def exists_word(word, instance):
    report = []
    for file in instance.queue():
        occurrences = search_word_in_file(word, file)
        if occurrences:
            report.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": [
                        {"linha": occurrence["linha"]}
                        for occurrence in occurrences
                    ],
                }
            )
    return report


def search_by_word(word, instance):
    report = []
    for file in instance.queue():
        occurrences = search_word_in_file(word, file)
        if occurrences:
            report.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return report


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    print("\n" + "*" * 100 + "\n")

    print("palavra existente apenas a linha:")
    print(exists_word("pedro", project))
    print("\n" + "*" * 100 + "\n")
    print("palavra existente com conteudo:")
    print(search_by_word("pedro", project))
    print("\n" + "*" * 100 + "\n")

    print("palavra inexistente:")
    print(search_by_word("Ratinho", project))
    print(exists_word("Ratinho", project))
