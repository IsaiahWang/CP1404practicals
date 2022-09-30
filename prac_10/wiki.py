import wikipedia
from wikipedia import DisambiguationError


def main():
    phrase = input('Type in the phrase you want to search: ')
    while phrase != '':
        try:
            page = wikipedia.page(phrase, auto_suggest=False)
            print('---------title---------')
            print(page.title)
            print('--------summary--------')
            print(page.summary)
            print('----------URL----------')
            print(page.url)
        except DisambiguationError:
            pass
        phrase = input('Type in the phrase you want to search: ')


main()