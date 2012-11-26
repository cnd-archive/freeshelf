from fabric.api import run, env, cd, hosts, execute, prefix

remote_dir = '/home/web/freeshelf.com'
venv_cmd = 'source ./env/bin/activate'
env.user = 'web'

def pull_code():
    with cd(remote_dir):
        run('git pull origin master')

def install_reqs():
    with cd(remote_dir):
        with prefix(venv_cmd):
            run('pip install -r requirements.txt')

def migrate():
    with cd(remote_dir):
        with prefix(venv_cmd):
            run('python manage.py syncdb')
            run('python manage.py migrate')

def collectstatic():
    with cd(remote_dir):
            with prefix(venv_cmd):
                run('python manage.py collectstatic --noinput -v 0')

def restart():
    with cd(remote_dir):
        run('touch freeshelf/wsgi.py')

@hosts('freeshelf.com')
def setup():
    run('git clone git@github.com:crnixon/freeshelf.git %s' % remote_dir,
        warn_only=True)
    with cd(remote_dir):
        run('virtualenv-2.6 --distribute env')

@hosts('freeshelf.com')
def deploy():
    execute(pull_code)
    execute(install_reqs)
    execute(migrate)
    execute(collectstatic)
    execute(restart)
