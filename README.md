## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

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

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `python3 manage.py test`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Deploiement
Le déploiement d'applications, également connu sous le nom de déploiement de logiciels, est le processus d'installation, de configuration, de mise à jour et d'activation d'une application ou d'une suite d'applications qui rendent un système logiciel disponible, comme la garantie d'une certaine URL sur un serveur.

### Configuration requise:
Pour un deploiement optimal de l'application, certaine brique technologique:

- Un compte Dockerhub, et docker d'installé sur votre machine:
    - https://docs.docker.com/get-docker/
  
- Un compte Circle-ci connecté avec le github lié au projet:
    - https://circleci.com/signup/    (Se connecter avec votre github)

- Un compte Heroku:
    - https://signup.heroku.com/

- Un compte Sentry:
    - https://sentry.io/signup/

### Etapes du deploiement:
### Etape 1:
Allez sur Heroku, cree un app avec ce nom excatement:
'oc-lettings-3000'
Ensuite suivez l'etape 2.
#### Etape 2:
Se connecter a Circle-ci avec votre compte Github>
Puis cliquez sur le boutton 'Set Up Project'
Selectionez le premier choix 'Fastest'
Le deployment va se lancer.

Des que Circle-ci montre un succes.

Retournez sur heroku.

Au niveau du dashboard de l'app cree precedement
cliquer sur Open app en haut à droite.

ou rendez-vous a cette adresse:
https://oc-lettings-3000.herokuapp.com/

### Sentry
installer heroku cli dans votre machine:
https://devcenter.heroku.com/articles/heroku-cli

Dans la console de votre venv :
```cython
heroku addons:create sentry
```
Aller sur ce lien, vous allez rencontrer une erreur, c'est normal.
https://oc-lettings-3000.herokuapp.com/sentry-debug/

Aller sur le dashboard Heroku de l'app:
et dans la catégorie 'Installed add-ons', cliquer su Sentry, vous serai rediriger sur le dashboard>









#### Etapes pour le telchargement local:

Apres avoir cloner le repo plus haut.
Connectez - vous au dockerHub, et faire la recherche 
``
gatsfreecs
``
dans la bare de recherche puis copier le pull de la dernière images dans le terminal :

exemple:
```cython
docker pull gatsfreecs/hash:2925ec5109e08d3cddf30032b5bfe1c2b581752a
```

Lancer le container en local
 
```cython
docker run --publish 8000:8000 gatsfreecs/hash:2925ec5109e08d3cddf30032b5bfe1c2b581752a
```
Dans votre navigateur mettre cette url : 0.0.0.0:8000




