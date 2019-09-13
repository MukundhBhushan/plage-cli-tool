from googletrans import Translator

class convclass:

    def conv(inp):
        translator = Translator()
        #inp = input("enter text: ")

        translations = translator.translate(inp, dest='de')
        translations = translator.translate(translations.text, dest='eo')
        translations = translator.translate(translations.text, dest='fr')
        translations = translator.translate(translations.text, dest='en')

        return(translations.text)

