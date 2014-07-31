from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
#env.input_path = 'docs'
env.deploy_path = 'site'
#DEPLOY_PATH = env.deploy_path

# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

#def clean():
#    if os.path.isdir(DEPLOY_PATH):
#        local('rm -rf {deploy_path}/*'.format(**env))
#        #local('mkdir {deploy_path}'.format(**env))
#    local('pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env))

def build():
    local('mkdocs build')

def serve():
    local('mkdocs serve')

def reserve():
    build()
    serve()

def pu2pages():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            'git st && '
            'git add --all . && '
            'git ci -am "upgrad from local. @MBP111216ZQ" && '
            'git pu && '
            'pwd '.format(**env)
          )

#env.qiniu = '/opt/bin/7niu_package_darwin_amd64/qrsync'
#env.qiniu_conf = '../7niu-pycon.json'
#env.qiniu_path = '../7niu.pyconcn'
#def put7niu():
#    build()
#    local('cd {qiniu_path} && '
#            'pwd && '
#            'python gen4idx.py ./ footer-7niu.html 2014 && '
#            '{qiniu} -skipsym {qiniu_conf}&& '
#            'pwd '.format(**env)
#          )


#def cf_upload():
#    rebuild()
#    local('cd {deploy_path} && '
#          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#          '-U {cloudfiles_username} '
#          '-K {cloudfiles_api_key} '
#          'upload -c {cloudfiles_container} .'.format(**env))

#@hosts(production)
#def publish():
#    local('pelican -s publishconf.py')
#    project.rsync_project(
#        remote_dir=dest_path,
#        exclude=".DS_Store",
#        local_dir=DEPLOY_PATH.rstrip('/') + '/',
#        delete=True
#    )

# Remote server configuration
#   deploy in obp hosting
#env.hosts = ['cn.pycon.org']
#env.port = 9022
#env.user = 'pycon'
#code_dir = '/opt/www/PyChina'

#def pub2cafe():
#    with cd('{deploy_path}'.format(**env)):
#        run('git add . ')
#        run("git ci -am 'upgraded in local.' " )
#        run("git pu cafe gitcafe-page" )

