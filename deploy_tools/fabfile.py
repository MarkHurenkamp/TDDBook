import random

import utils.config_reader as config_reader
from fabric.api import cd, env, local, run
from fabric.contrib.files import append, exists

config = config_reader.Config.load_json("config.json")

env.host = config.host
env.host_string = config.host_string
env.user = config.user
env.key_filename = config.key_filename



REPO_URL = 'https://github.com/MarkHurenkamp/TDDBook/tree/pbitest'

def deploy():
    run('uptime')
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtual_env()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source() -> None:
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')

def _update_virtual_env() -> None:
    if not exists('venv/bin/pip'):
        run(f'python3 -m venv venv')
    run('./venv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv() -> None:
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files() -> None:
    run('./venv/bin/python manage.py collectstatic --noinput')

def _update_database() -> None:
    run('./venv/bin/python manage.py migrate --noinput')
