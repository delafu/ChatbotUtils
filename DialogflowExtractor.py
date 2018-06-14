import json
import glob

files = glob.glob('*usersays_es.json')
result = open('smalltalk.tsv', 'w')
for fichero in files:
    with open(fichero) as data_file:
        print(fichero)
        data = json.load(data_file)
        for entry in data:
            print(entry)
            frase = entry['data'][0]['text']
            result.write(frase + '\t'+ fichero + '\n')
result.close()