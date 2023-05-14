# Welcome

This script based on Django Framework for seo audit tools and scrape latest news from CNN. Before we start make sure your machine has Docker and `docker-compose` installed before.

## How to install

For easy run and cross platform support we use Docker for manage containers. Let's go!

- Pull this repository
- Navigate to root folder where `docker-compose.yml` exist
- Run `docker-compose -f docker-compose.yml up -d`
- Wait until all process finish
- Navigate to `http://localhost:9000`

## Create super-admin user

As default Django don't create super-admin user, so we must create it.

- Open CMD (or Power Sheel) / whatever you have
- Copy `docker ps` then enter
- Get container name or id with word `backend`
- Copy the name or id
- Copy `docker exec -it <container name/id> bash` hit enter
- If success you will entered into container terminal
- Copy `python manage.py createsuperuser` hit enter and follow instructions
- Done

## Access admin dashboard

Django provided default dashboard

- Open `http://localhost:9000/admin`
- Enter username and admin created before (super-admin)

## Run CNN scraper

To get latest news from CNN run this

- Open `http://localhost:9000/auditor/getnews/`
- Wait until return results with contains links successed scraped
- Back to `http://localhost:9000/admin` navigate to menu `News` to see scraper results

## Final word

This script not perfect, if you have idea make pull-request. Thank you.
