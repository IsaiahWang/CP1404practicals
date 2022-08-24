"""
CP1404 Practical 5
Count word occurrences in a string
"""


def main():
    """Start of program."""
    text = input('Text: ')
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    # method 2
    # for word in words:
    #     if word in word_to_count:
    #         word_to_count[word] += 1
    #     else:
    #         word_to_count[word] = 1

    word_count_sorted = sorted(word_to_count.items())
    # word_dict_sorted = sorted(word_dict.items(), key=lambda x: x[0])
    # word_dict_sorted = sorted(word_dict.items(), key=operator.itemgetter(0))
    max_length = max((len(word) for word in word_to_count.keys()))
    for item in word_count_sorted:
        print(f'{item[0]:{max_length}} : {item[1]}')


main()
