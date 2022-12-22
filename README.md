## Résumé

Website Orange County Lettings

## Local Developement 

### Requirements

- 
GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 ou more

In the rest of the local development documentation, it is assumed that your OS shell's `python` command runs the Python interpreter above (unless a virtual environment is enabled).

### macOS / Linux

#### Clone le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Create virtual environement:

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Run the website

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Unit Tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `python3 manage.py test`

#### DataBase

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Admnistration panel

- Go here `http://localhost:8000/admin`
- Connected with user : `admin`, password : `Abc1234!`

### Windows

Use the PowerShell, like this :

- For activate the virtual environement, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` by `(Get-Command <my-command>).Path`

## Deployment
Application deployment, also known as software deployment, is the process of installing, configuring, updating, and activating an application or suite of applications that makes a system software available, such as guaranteeing a certain URL on a server..

### Required configuration:
For an optimal deployment of the application, certain technological brick:

- A Dockerhub account, and docker installed on your machine:
    - https://docs.docker.com/get-docker/
  
- A Circle-ci account connected with the github linked to the project:
    - https://circleci.com/signup/ (Sign up with your github)

- A Heroku account:
    - https://signup.heroku.com/

- A Sentry account:
    - https://sentry.io/signup/

### Deployment steps:
### Step 1:
Go to Heroku, create an app with this exactly name:
'oc-lettings-3000'

### Sentry
install heroku cli in your machine:
https://devcenter.heroku.com/articles/heroku-cli

In the console of your venv:
```cython
heroku addons:create sentry --app oc-lettings-3000
```
and open page with :
```cython
heroku addons:open sentry  
```
a window opens and follow the steps for Django,
fill in copy only the digits of the DSN url in the project settings.

example :
you will have something like this:

```dsn="https://3a11a3a2f0da47b4942e96a7081f2d8b@o45043688865792.ingest.sentry.io/4504368886579200",```


please fill in the settings variable:

keys_1 = '3a11a3a2f0da47b4942e96a7081f2d8b@o45043688865792'
keys_2 = '4504368886579200'


And this every time, because the url changes every time you change the app.

Redo an **git add, commit, push, each time you touch the settings.**


#### 2nd step:
Connect to Circle-ci with your Github account >
Then click on the 'Set Up Project' button
Select the first choice 'Fastest'
The deployment will start.

As soon as Circle shows success.

Go back to heroku.

At the level of the dashboard of the app created previously
click on Open app at the top right.

or go to this address:
https://oc-lettings-3000.herokuapp.com/

Go to this link, you will encounter an error, this is normal.
https://oc-lettings-3000.herokuapp.com/sentry-debug/

return to the sentry page previously (sentry page previously spoken) and view the errors

#### Steps for local download:

After cloning the repo above.
Login to dockerHub, and do the search
``
gatsfreecs
``
in the search bar then copy the sweater of the last images in the terminal:

exemple:
```cython
docker pull gatsfreecs/hash:2925ec5109e08d3cddf30032b5bfe1c2b581752a
```

run the container localy:
 
```cython
docker run --publish 8000:8000 gatsfreecs/hash:2925ec5109e08d3cddf30032b5bfe1c2b581752a
```
On your web browser put this url : 0.0.0.0:8000 or localhost:8000




