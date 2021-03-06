from fabric.context_managers import cd, prefix
from fabric.operations import sudo, run
from fabric.state import env

PROJECT_NAME = ''
PROJECT_ROOT = ''
VENV_DIR = ''
REPO = ''


def update():
    env.host_string = ''
    env.user = ''
    env.password = ''
    with cd(PROJECT_ROOT):
        sudo('git stash')
        sudo('git pull origin master')
        with prefix('source ' + VENV_DIR + '/bin/activate'):
            run('pip install -r requirements/prod.txt')
            run('./manage.py collectstatic --noinput')
            run('./manage.py migrate')
            sudo('service uwsgi restart')