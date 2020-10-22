import paramiko
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('Kuai - Backup'))

deviceip = input("what's the IP of your device?: ")
devicerootpass = input("what's the root password?: ")

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(deviceip, "22", "root", devicerootpass)
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && mkdir backup')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && cp ./apple-logo-n84@2x~iphone.png ./backup/')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && cp ./apple-logo-black-n84@2x~iphone.png ./backup/')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && cp ./apple-logo-black@2x~iphone.png ./backup/')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && cp ./apple-logo@2x~iphone.png ./backup/')
    return client

ssh = createSSHClient(deviceip, "22", "root", devicerootpass)
print("backup sucessfully completed!")
