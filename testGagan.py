from fabric.api import *

env.hosts = ['172.20.29.230']
env.user = 'node'
env.key_filename = r'C:\Users\devapga\.ssh\Gagan-230\id_rsa'

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')