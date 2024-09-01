# POC django backend basic auth, simple jwt, proxy model

 * poetry is used for library version management in poetry.lock file
 * direnv to load secrets from envrc
 * docker for local development purpose
 * black, isort, flake8 for linting in pre-commit hook
 * drf_spectacular swagger api https://{host}/api/docs/#tag/users
 * postgres:14.7 for relational database


REST api to service to sevice / FE BE communication for managing a game
in this POC, the game consist of league with log(2^N) elimination rounds
There can be any power of 2 Teams, i.e: 16 Teams
in each round 2 teams can participate, and one moves forward, thus there are ln(N) rounds

There can be three types of users: League Admin, Coach (can manage only one team), Player.

Users(Player, Coach, LeagueAdmin), Teams, Leagues, Games and Rounds are the basic business models.  
 

A team can consist of many players but at a league certain number of players say 5 (basketball) 
can participate. 
If A team participates in multiple leagues, some player may participate in some of the
leagues. Each individual participation is recorded in player details model. 
A winning team should keep its participants winning record updated as well, others whom did not participated
on that league remains usual.

A game represents each elimination round, record of winning and losing team on that round.
A round represents match count, game and league to rebuild the score board of each league.

Authorization are enforced in custom permission_class, 
also JWT claims are updated with user type ( player, coach, league admin ) for facilitating stateless service to service communication.

Management scripts i.e: init_game  is written for end2end integration and demo in users app.

Migration history represents the unfolding relations and business logic of models.
 
 
Next Phase: Tests cases are must to be written, implement full functionality exposing necessary api with authorization
representing init_game management script.
Implementation of Front End, preferrably NextJS in React or any convenience.  

#### build virtualenv, run app and rds in docker, run migration, initate management script

```bash
setup test environment config

DJANGO_SETTINGS_MODULE=matgame.settings;DJANGO_DEBUG=TRUE
```

```bash
poetry install
poetry lock --no-update
poetry show -v
source {venv path}/bin/activate
```


#### docker compose  location
```bash
/local/
```

####  gunicorn runserver
```bash
please check dockerfile for multistage build, entry.sh for gunicorn run of wsgy  
```

```bash 
python manage.py makemigrations
python manage.py migrate

python mange.py init_game
```

#### Regards: geass.of.code@gmail.com 


