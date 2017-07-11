#!/usr/bin/env python
import os
import sys

from BeautifulSoup import BeautifulSoup
import requests

def scrape():
    url = "http://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos/"
    soup = BeautifulSoup(requests.get(url).text)
    team_count = 1 
    
    #for team in soup.find(id="team").children[3].children:
    for team in soup.find(id="team").findAll("li"):
        team_url = "http://www.sportslogos.net/{}".format(team.a['href'])
        team_soup = BeautifulSoup(requests.get(team_url).text)
        for logos in team_soup.findAll("ul", {'class':'logoWall'}):
            print "{} count={}".format(logos,team_count)
        team_count = team_count + 1

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbatrader.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    scrape()
