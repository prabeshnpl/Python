# language codes:
# zh Chinese, en English , es Spanish , pt Portuguese

from translate import Translator 
translator=Translator(to_lang='ja')

try:
    with open('projects/plain.txt','r') as my_file:
        with open('projects/translated_text.txt','w',encoding='utf-8') as my_file2:
            for lines in my_file:
                translated=translator.translate(lines)
                my_file2.write(f'{translated}\n')
            
except FileNotFoundError as err:
    print(f'File is not there you fool,\n{err}')
