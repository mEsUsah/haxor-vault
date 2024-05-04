# Vault Haxor
Simple webapp for storing encrypted credentials


# Getting Started
## Installation
```bash
# Install build essentials (Linux Debian/Ubuntu)
sudo apt-get install python3-dev python3-venv default-libmysqlclient-dev build-essential pkg-config libxml2-dev

# Setup log directory
sudo mkdir -p /var/log/django/vault.haxor.no/

# Install Python dependencies
python3 -m venv venv
chmod +x venv/bin/activate 
source venv/bin/activate
pip install -r requirements.txt

# Install JavaScript dependencies
npm install
```

## MySQL / MariaDB setup
```SQL
-- Crate DB
CREATE DATABASE vaulthaxor;

-- Local database user
CREATE USER vaulthaxor@localhost IDENTIFIED BY 'vaulthaxor';
GRANT ALL PRIVILEGES ON vaulthaxor.* TO vaulthaxor@localhost;
FLUSH PRIVILEGES;

-- WSL database user
CREATE USER vaulthaxor@'%' IDENTIFIED BY 'vaulthaxor';
GRANT ALL PRIVILEGES ON vaulthaxor.* TO vaulthaxor@'%';
FLUSH PRIVILEGES;
```

## Setup
Copy the example .env file, and add correct data.
```bash
# Create .env file
cp .env.example .env

# Edit .env file
vim .env
```

Populate DB with tables and base data.
```bash
# Crate DB tables and add basic data
python3 manage.py migrate

# Create superuser account
python3 manage.py createsuperuser
```

# Dev
## Start developing
In the .env file set the follownig variables
```Dotenv
DEBUG=True
DEV_MODE=True
S3_ACTIVATED=False
```

Start services.
```bash
# start python devserver
python3 devsearch/manage.py runserver

# In separte shell
npm run dev

# The site will be accessable (with live reload) at http://localhost:8000
```

# Prod
## Build assets
```bash
npm run prod
```

## Sync static files to S3 bucket
```bash
python3 manage.py collectstatic -v 2 --no-input
```


## Env. variables
In the .env file set the follownig variables
```Dotenv
DEBUG=False
DEV_MODE=False
S3_ACTIVATED=True
```

## Runs uWSGI server
```bash
uwsgi --socket streakhaxor.sock  --module streakhaxor.wsgi --chmod-socket=666
```

## Deploy new commits
```bash
sudo -u www-data git pull
sudo supervisorctl restart streak_haxor
```

# Cleanup / Uninstalling
## Uninstall 
```bash
deactivate
```

## Update Python dependency list
```bash
pip freeze > requirements.txt
```

# Resourcese
* [django-storages](https://django-storages.readthedocs.io/en/latest/)
* [django-vite-plugin](https://github.com/protibimbok/django-vite-plugin)