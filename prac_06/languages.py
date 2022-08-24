"""
CP1404/CP5632 Practical
Programming Language client code.
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Start of a program."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)
    programming_languages = [ruby, python, visual_basic]
    # dynamic_type_languages = list(filter(lambda a: (a.typing == 'Dynamic'), programming_languages))
    dynamic_type_languages = [language for language in programming_languages if language.typing == 'Dynamic']
    print('The dynamically typed languages are:')
    for language in dynamic_type_languages:
        print(language.name)


main()
