def replace_word():

    str = "gaiola aberta. aberta a janela. o pássaro desperta, a vida é bela. a vida é bela, a vida é boa. voa, pássaro, voa."

    word_to_replace = input('palavra para substituir: ')
    word_replacement = input('palavra que substutuiu: ')
    print(str.replace(word_to_replace, word_replacement))

replace_word()