import operator


def main():
    text = input('Text: ')
    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict.update({word: word_dict.get(word) + 1})
        else:
            word_dict.update({word: 1})
    word_dict_sorted = sorted(word_dict.items())
    max_length = max([len(word) for word in word_dict.keys()])
    for item in word_dict_sorted:
        print(f'{item[0]:{max_length}} : {item[1]}')
    # method 2
    # word_dict_sorted = sorted(word_dict.items(), key=lambda x: x[1])
    # for item in word_dict_sorted:
    #     print(f'{item[0]} : {item[1]}')

    # method 3
    # word_dict_sorted = sorted(word_dict.items(), key=operator.itemgetter(1))
    # for item in word_dict_sorted:
    #     print(f'{item[0]} : {item[1]}')


main()
