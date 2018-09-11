from fabric import Connection
#ssh -o StrictHostKeyChecking=no node@172.20.29.230
#c=Connection(host='172.20.29.230', user='node', connect_kwargs={'password': r'node'})
c=Connection(host='172.20.29.230', user='node', connect_kwargs={'key_filename': r'C:\Users\devapga\.ssh\230\id_rsa'})
c.run('df -h')