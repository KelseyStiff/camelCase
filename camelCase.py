def camelcase(sentence):
    title_case = sentence.title() #uppercase
    upper_camel_cased = title_case.replace(' ', '')
    return upper_camel_cased[0:1].lower() + upper_camel_cased

def banner():
    """ Display welcome Banner """
    message = "CAMELCASE PROGRAM"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')

def main():
    banner()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)



main()

