from fabric.api import env, run, put, local, cd, sudo

env.hosts = ['loogica.net']

def zip_output():
    local('zip -r blog_static.zip output')

def send_data():
    put('blog_static.zip', '/tmp')

def remote_deploy_zip():
    sudo('mv /tmp/blog_static.zip /opt/apps/blog')
    with cd('/opt/apps/blog'):
        sudo('rm -rf old_output/')
        sudo('mv output old_output')
        sudo('unzip blog_static.zip')

def deploy():
    zip_output()
    send_data()
    remote_deploy_zip()
