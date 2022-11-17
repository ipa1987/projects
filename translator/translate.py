from translate import Translator

languages = ['gu','hi', 'ar', 'ja', 'tr']

text = input("enter your sentence :  ")

for language in languages:

  lan=Translator(from_lang='en', to_lang=language)
  
  resu = lan.translate(text)

  print(f'{language}: {resu}')