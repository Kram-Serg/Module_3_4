
def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        if word.upper().count(root_word.upper()) >= 1:
            same_words.append(word)
            continue
        elif root_word.upper().count(word.upper()) >= 1:
            same_words.append(word)
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)