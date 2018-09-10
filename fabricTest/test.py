from fabric.api import local, run, task, roles

@task
def local_uname():
    local('uname -a')

@roles('foo')
@task
def remote_uname():
    run('uname -a')