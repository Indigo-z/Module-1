def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_words.append(word)

    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
