import re
import os

path = os.path.join(os.getcwd(), 'wiki_test')

for filename in os.listdir(path):
    if filename.endswith('.html'):
        with open(os.path.join(path, filename), 'r') as file:
            data = file.read()
            # for some reason using a capture group messed this up, but this is a 
            # prototype after all
            out = set(re.findall("<a href=\"(?:https:\/\/en.wikipedia.org)?\/wiki\/(?:Category:)?\w+\"", str(data)))

            print(filename)
            with open(os.path.join(path, filename + '.reduced'), 'w') as output:
                for item in out:
                    item = re.sub("<a href=\"(?:https:\/\/en.wikipedia.org)?\/wiki\/",'',item)[:-1]
                
                    print(f'\t {item}')
                    output.write(item + '\n')

