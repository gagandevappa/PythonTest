from fabric.api import env

env.use_ssh_config = True
env.forward_agent = True

env.roledefs = {
    # key   # hostname from config
    'foo': ['foo.production'],
}