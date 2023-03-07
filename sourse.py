from sys import argv
from os import path
import openai #paste cmd 'pip install openai'

openai.api_key = "ChatGPT API KEY" 

prom = "write a blog post for" #Приставка для ключа

def getAI(key):
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prom + " " + key,
                                          temperature=0.5,
                                          max_tokens=1000)
    return(completion.choices[0]['text'])

def writeF(key, kontent):
    end_path = key + ".txt"
    if(path.exists(end_path)):
        print("Потеря файла: '" + end_path + "'")
    else:
        f = open(end_path, 'w')
        f.write(kontent)
        f.close()
        
if(len(argv) == 2):
    file_path = argv[1]
    print("Запуск для файла: " + file_path)
    if(path.exists(file_path)):
        print("Получение ключей...")
        f = open(file_path, 'r')
        keys = f.read().split("-") #Розделитель при чтение с файла
        f.close()
        for key in keys:
            print("Генерация для ключа: '" + key + "'")
            writeF(key, getAI(key))
            print("Згенерировано: '" + key + "' !")
    else:
        print("Указаний файл не найден !")
else:
    print("Использование: " + argv[0] + " 'file_path'")
