import os
import re

path = os.path.join(os.getcwd(), 'wiki_test/')
file_ending = '.html.reduced'

start = 'Fly'
dest = 'Silk'

visited = []
queue = []

visited.append(start)
queue.append(start)

while queue:
    m = queue.pop(0).strip('\n')
    print(m, end=' ')
    
    try:
        with open(path + m + file_ending, 'r') as file:
            data = file.readlines()
            for item in data:
                if item not in visited:
                    visited.append(item)
                    queue.append(item)
    except:
        continue




    

