def backward_string_by_word(text: str) -> str:
    # text = text.split()
    #
    #
    # # text.split()
    # print(text)
    # answer = list()
    # for word in text:
    #     answer.append(word[::-1])
    return ' '.join([word[::-1] for word in text.split()])


print("he\tllo  \n wor \t ld")

backward_string_by_word("he\tllo  \n wor \t ld")