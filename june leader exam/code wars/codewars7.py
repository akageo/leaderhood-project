def abbreviate(text):
    word = ""
    text2 = ""
    for i in text:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            word += i
        elif i not in "abcdefghijklmnopqrstuvwxyz" or i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if len(word) >= 4:
                word_a10n = word[0] + str(len(word) - 2) + word[-1]
                text2 += word_a10n
            else:
                text2 += word
            word = ""
            text2 += i
    if len(word) >= 4:
        word_a10n = word[0] + str(len(word) - 2) + word[-1]
        text2 += word_a10n
    else:
        text2 += word
    return text2