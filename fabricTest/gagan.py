from fabric.api import *
env.hosts = ['172.20.29.230']
env.user = 'node'
env.key_filename = r'C:\Users\devapga\.ssh\VM-230.ppk'

def local_uname():
    local('uname -a')
