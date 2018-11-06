import requests;
import click;
import json;
import pdb;

URL = 'https://personal-dashboard-umbrella-kino6052.c9users.io'

def getCalendarEvent(year, month, day):
    item = requests.get('{}/calendar/{}/{}/{}'.format(URL, year, month, day)).json()
    return item[0]
        
        
@click.command()
@click.option('--year', prompt=True, default=2018, help='Year of the Event')
@click.option('--month', prompt=True, default=1, help='Month of the Event')
@click.option('--day', prompt=True, default=1, help='Day of the Event')
def print_calendar_event(year, month, day):
    print getCalendarEvent(year, month, day);

if __name__ == '__main__':
    print_calendar_event(year, month, day)
    
# 5b6605a886ec2e1a5a713867