[project overview video ](https://drive.google.com/file/d/1HLApzEDwIP_oujvCMssmym2S2IlUl0SY/view?usp=sharing)
#### POC: Management system for simple game of elimination rounds


```
 techstak: django
 * REST api versioned for stateless resource management
 * jwt as auth, proxy model for custom user types.
 * poetry is used for library version management in poetry.lock file
 * direnv to load secrets from envrc
 * docker for local development purpose
 * black, isort, flake8 for linting in pre-commit hook
 * drf_spectacular swagger api https://{host}/api/docs/#tag/users
 * postgres:14.7 for relational database
 
 containerize in docker for local dev
 
```



The game consist of leagues, event of log(2^N) elimination rounds
There can be N teams, where N is power of 2.
i.e: A league of 16 Teams, can have ln(16) = 2^4 = 4 rounds
In each round, each pair of teams contends and one wins eliminating the other.

In this business model there are three types of users: League Admin, Coach (can manage only one team), and Player.

A team may have multiple players but at each game a fixed number of palyer can participate.
Individual participants have player statistics like winning and number of participation count.

```
Management scripts is written for end2end integration and demo

script location: i.e: users/management/commands/init_game

python manage.py init_game 
```
TODO:
Implementation of Front End, preferrably NextJS in React or any convenience.
Enhance with all necessary API.

```
schema:
```
![schema game models](https://github.com/user-attachments/assets/34acf5f1-d259-4605-af98-3faf9383594a)


#### local development 

```bash

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


