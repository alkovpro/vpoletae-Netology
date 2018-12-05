import requests

def translator(path_in, path_out, lang_from, lang_to = 'ru'):

    with open(path_in, 'r', encoding = 'UTF8') as f:
        text = f.read()

    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': text,
    }

    try:      
        response = requests.post(URL, data = {'text': text}, params = params)
        answer = response.json()

        with open(path_out, 'w', encoding = 'UTF8') as f:
            for line in answer['text']:
                f.writelines(line)
    except:
        print('Something went wrong! Please check data inputs')
        main()


def main():
    path_in = input("Please copy a path to a file, you'd like to translate: ")
    path_out = input("Please point out a path, where you'd like to place translated file: ")
    lang_from = input("From which language would you like to translate a file: ")
    lang_to = input("In which language would you like to make a translation (if missed - used Russian): ")

    translator(path_in, path_out, lang_from, lang_to = 'ru')

if __name__ == '__main__':
    main()
