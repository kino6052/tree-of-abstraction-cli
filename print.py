import requests;
import click;
import json;
import pdb;

URL = 'https://personal-dashboard-umbrella-kino6052.c9users.io'

def getItem(id):
    item = requests.get('{}/item/{}'.format(URL, id)).json()
    return item[0]
    
def getItemByTitle(title):
    item = requests.get('{}/item?title={}'.format(URL, title)).json()
    return item[0]

def getNotesForItem(id):
    notes = []
    item_notes = requests.get('{}/item-note?itemId={}'.format(URL, id)).json()
    for item_note in item_notes:
        note_id = item_note[u'noteId']
        note = requests.get('{}/note/{}'.format(URL, note_id)).json()[0]
        notes.append(note)
    return notes
    
def printNotesForItem(id, indent):
    item_notes = requests.get('{}/item-note?itemId={}'.format(URL, id)).json()
    for item_note in item_notes:
        note_id = item_note[u'noteId']
        note = requests.get('{}/note/{}'.format(URL, note_id)).json()[0]
        click.secho(note[u'title'], fg='white', bg='black')
        click.secho(note[u'_id'] + '\n')
        click.secho(note[u'content'])

def getNode(id_tuple):
    id = id_tuple[0]
    indent = id_tuple[1]
    json_obj = getItem(id)
    title = json_obj[u'title'].encode('utf-8')
    # pdb.set_trace()
    click.secho('{}'.format('|\t'*indent + '|_'), nl=False)
    click.secho(' {} '.format(title), fg='red', bg='white', nl=False)
    click.secho(' {} '.format(id), fg='white')
    return json_obj
    
def getChildren(json_node, indent):
    children = []
    result = []
    # pdb.set_trace()
    if u'children' in json_node:
        children = json_node[u'children']
    for child in children:
        child = child.encode('utf-8')
        result.append((child, indent))
    return result
    
def print_tree_with_depth(id, depth, notes):
    stack = [(id, 0)]
    while True:
        try:
            if len(stack) == 0:
                break;
            cur_id = stack.pop()
            indent = cur_id[1]
            if indent >= depth:
                continue
            json_node = getNode(cur_id);
            if notes:
                printNotesForItem(cur_id[0], indent + 1)
            children = getChildren(json_node, indent + 1);
            stack = stack + children
        except Exception:
            print 'exception';
            continue;
        
        
@click.command()
@click.option('--id', prompt=True, default='5b6605a886ec2e1a5a713867', help='id of a Node')
@click.option('--title', help='Title to search')
@click.option('--depth', prompt=True, default=0, help='Depth of the tree to show')
@click.option('--notes', is_flag=True)
def print_tree(id, title, depth, notes):
    id = id.encode('utf-8')
    if title:
        title = title.encode('utf-8')
        item = getItemByTitle(title)
        item_id = item[u'_id']
        print_tree_with_depth(item_id, depth, notes)
    elif depth > 0 and depth <= 5:
        print_tree_with_depth(id, depth, notes)

if __name__ == '__main__':
    print_tree()
    
# 5b6605a886ec2e1a5a713867