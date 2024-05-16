def exists_word(word, instance):
    found_in_list = []
    lines = []
    for index in range(len(instance)):
        file = instance.search(index)
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                lines.append({"linha": i + 1})
        if len(lines) == 0:
            return found_in_list
        found_in_list.append(
            {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines,
            }
        )
    return found_in_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
