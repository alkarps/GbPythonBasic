words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def translate(line):
    _words = line.split()
    _words[0] = words[_words[0]]
    return " ".join(_words)


with open("part4.txt", "r", encoding="utf-8") as origin:
    with open("part4_new.txt", "w", encoding="utf-8") as source:
        source.writelines([translate(x) + "\n" for x in origin.readlines()])
