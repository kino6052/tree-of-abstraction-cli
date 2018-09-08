import requests;
import click;
import json;
import pdb;

URL = 'https://personal-dashboard-umbrella-kino6052.c9users.io'

def postItem(title):
    payload = { 'title': title.encode('utf-8') }
    item = requests.post('{}/item'.format(URL), json=payload).json()
    return item

def addItemAsChild(parent_id, child_id):
    item = requests.put('{}/item/{}/{}'.format(URL, parent_id, child_id)).json()
    return item
        
@click.command()
@click.option('--id', prompt=True, help='id of the parent node')
@click.option('--title', prompt=True, help='title of the node')
def add_item(id, title):
    if id is not None and title is not None:
        item = postItem(title)
        item_id = item[u'_id']
        addItemAsChild(id, item_id)
        
if __name__ == '__main__':
    add_item()