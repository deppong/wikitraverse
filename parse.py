import re

with open('wiki_test/Eutreta_fenestra.html', 'r') as file:
    data = file.read()
    # for some reason using a capture group messed this up, but this is a 
    # prototype after all
    out = set(re.findall("\"\/wiki\/C?a?t?e?g?o?r?y?:?\w+\"", str(data)))

    for item in out:
        item = item[7:-1]
        print(item)

