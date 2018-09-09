import requests;
import click;
import json;
import pdb;

URL = 'https://personal-dashboard-umbrella-kino6052.c9users.io'

@click.command()
@click.option('--parent_id', prompt=True, help='parent of a node to be removed')
@click.option('--child_id', prompt=True, help='node to be removed')
def delete_item(parent_id, child_id):
    if parent_id is not None and child_id is not None:
        item = requests.delete('{}/item/{}/{}'.format(URL, parent_id, child_id)).json()
        return item
        
if __name__ == '__main__':
    delete_item()