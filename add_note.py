import requests;
import click;
import json;
import pdb;

URL = 'https://personal-dashboard-umbrella-kino6052.c9users.io'

def create_note(title, content):
    payload = { 
        'title': title.encode('utf-8'),
        'content': content.encode('utf-8')
    }
    item = requests.post('{}/note'.format(URL), json=payload).json()
    return item

def connect_item_and_note(itemId, noteId):
    payload = { 
        'itemId': itemId.encode('utf-8'),
        'noteId': noteId.encode('utf-8')
    }
    item = requests.post('{}/item-note'.format(URL), json=payload).json()
    return item
        
@click.command()
@click.option('--id', prompt=True, help='id of the parent node')
@click.option('--title', prompt=True, help='title of the note')
def add_item(id, title):
    if id is not None and title is not None:
        content = click.edit('Enter text of the note')
        note = create_note(title, content)
        note_id = note[u'_id']
        connect_item_and_note(id, note_id)
if __name__ == '__main__':
    add_item()