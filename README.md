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

De volgende functionaliteiten staan op de 'roadmap'.

- [ ] Uploaden van bestanden (PDF, JPG, ...) in plaats van gebruik van een link naar een CDN.
- [ ] Beheerpaneel in dezelfde stijl als de frontend.
- [ ] Markdown voor de checkpoint-tekst.
- [ ] Functionaliteit om de checkpoints op een kaart te tonen.
- [ ] Overzicht om QR-codes voor registratie van deelnemers en checkpoints te genereren.
- [ ] Aanmaken van meerdere hikes of evenementen, zodat niet iedere keer een nieuwe instantie gebruikt hoeft te worden.
- [ ] Registratieformulier gebruikers, zodat ook andere scoutinggroepen gebruik kunnen maken van het systeem.
- [ ] Overzicht voor organisatie om doorlooptijden van verschillende teams te bekijken, ook met behulp van een [team-standings diagram](https://commons.wikimedia.org/wiki/File:Team_Standings.png).

Voor de rest zijn de volgende functionaliteiten voor een IJsselgroepRally nog gewenst.
- [ ] Toevoegen puntentelling op basis van het aantal bezochte checkpoints.
- [ ] Toevoegen puntentelling op basis van een ander klassementsonderdeel. 

Volgende functionaliteiten zijn mooi om te hebben, maar staan nog niet op de roadmap.
- [ ] Toevoegen van progressive web-app functionaliteit.
  - [ ] In de app een QR-scan functionaliteit toevoegen.
- [ ] Realtime locatie met behulp van Javascript/websockets om de locatie van gebruikers te tracken als zij de website of progressive web-app open hebben, zodat de leiding kan zien bij welke supermarkt de deelnemers zitten.
- [ ] Methode om routes te delen (bewerkers- en inzagerechten administratiepaneel) en om te kopiëren naar een ander account, zodat je jouw mooie route met andere scoutinggroepen kunt delen, om deze bijvoorbeeld tijdens verhuur beschikbaar te stellen aan anderen.

## Lokaal draaien
Zorg ervoor dat je beschikt over Python 3.7 [lokaal geinstalleerd](http://install.python-guide.org). Om te pushen naar Heroku, moet je [Heroku CLI installeren](https://devcenter.heroku.com/articles/heroku-cli), alsmede [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/ScoutingIJsselgroep/rally.git

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py createsuperuser

$ DEBUG=true && python manage.py startserver debug
```

De app draait nu op [localhost:5000](http://localhost:5000/). Het administratiepaneel is beschikbaar op [localhost:5000](http://localhost:5000/admin).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
of

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
