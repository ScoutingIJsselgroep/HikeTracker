# HikeTracker

Een applicatie waar deelnemers met behulp van een QR-code checkpoints kunnen scannen. Hiermee kan de organisatie van bijvoorbeeld een hike in de gaten houden waar deelnemers al geweest zijn. Daarnaast kunnen deelnemers hun voortgang ten opzichte van andere teams in de gaten houden. 

## Functionaliteit
De volgende functionaliteit is al ingebouwd.

- [x] Beheerpaneel.
- [x] Overzicht van reeds bezochte checkpoints.
- [x] Overzicht van deelnemers die specifieke checkpoint hebben bezocht.
- [x] Het plaatsen van een marker op een kaart. 
- [x] Toevoegen van een hyperlink naar een document of aanwijzing.
- [x] Aanmaken van een custom link, om deze bijvoorbeeld als oplossing van een puzzel te gebruiken.
- [x] Deelnemers krijgen een melding als het gescande checkpoint door iedereen is bezocht, zodat deze mee kan worden genomen.

De volgende functionaliteit zal nog worden ingebouwd.

- [] Uploaden van bestanden (PDF, JPG, ...) in plaats van gebruik van een link.
- [] Markdown voor de checkpoint-tekst.
- [] Functionaliteit om de checkpoints op een kaart te tonen.
- [] Overzicht om QR-codes voor registratie deelnemers en 
- [] Aanmaken van meerdere hikes of evenementen, zodat niet iedere keer een nieuwe instantie gebruikt hoeft te worden.
- [] Registratieformulier gebruikers, zodat ook andere scoutinggroepen gebruik kunnen maken van het systeem.
- [] Overzicht voor organisatie om doorlooptijden van verschillende teams te bekijken, ook met behulp van een [team-standings diagram](https://commons.wikimedia.org/wiki/File:Team_Standings.png).

Voor de rest zijn de volgende functionaliteiten voor een IJsselgroepRally nog gewenst.
- [] Toevoegen puntentelling op basis van het aantal bezochte checkpoints.
- [] Toevoegen puntentelling op basis van een ander klassementsonderdeel. 

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/ScoutingIJsselgroep/rally.git

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ DEBUG=true && python manage.py startserver debug
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
