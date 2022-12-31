import os
import re
import wikipediaapi

wiki = wikipediaapi.Wikipedia('en')

def parse_links(links):
    out = []
    for title in sorted(links.keys()):
        out.append(re.sub(" \(id: ??.*", "", str(links[title])))

    return out

def sub_links(links, dest):
    visited = []
    for page in links:
        # get the sub page
        sub_page = wiki.page(page)
        print(sub_page.title)
        visited.append(sub_page.title)
        # if it's the destination we are done!
        if sub_page.title == dest:
            return visited
            

        sub_links = parse_links(sub_page.links)
        for item in sub_links:
            if item == dest:
                visited.append(item)
                return visited
            if item not in visited:
                visited.append(item)
                print('\t' + item)
    return visited


start = 'Odense'
dest = 'FaZe Clan'

start_page = wiki.page(start)

links = parse_links(start_page.links)

# where things might get hairy
print(dest in sub_links(links, dest))
