from fabric.api import env, run, put, local, cd, sudo

env.hosts = ['loogica.net']

def zip_output():
    local('zip -r blog_static.zip output')

def send_data():
    put('blog_static.zip', '/tmp')

def remote_deploy_zip():
    with cd('/tmp'):
        sudo('unzip blog_static.zip')
        sudo('mv output/ /opt/apps/')
    with cd('/opt/apps'):
        sudo('rm -rf videos')
        sudo('mv output videos')
        sudo('chown -R deploy:www-data videos')

def deploy():
    zip_output()
    send_data()
    remote_deploy_zip()
