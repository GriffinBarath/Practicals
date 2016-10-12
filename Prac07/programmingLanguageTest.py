from Prac07.programmingLanguage import ProgrammingLanguage


def main():
    programmingLanguages = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                            ProgrammingLanguage("Python", "Dynamic", True, 1991),
                            ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
    for language in programmingLanguages:
        print(language)
    print("The dynamically typed languages are:")
    for language in programmingLanguages:
        if language.isDynamic():
            print(language.name)


main()
