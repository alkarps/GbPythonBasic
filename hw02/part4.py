words = input("Please, input words: ").split(" ")
for i in range(len(words)):
    print(f"{i}'s word: {words[i][:10]}")
