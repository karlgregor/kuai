import paramiko
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('Kuai - Restore'))
print("MAKE SURE YOU HAVE A MADE BACKUP BEFORE USING BACKUP.PY!")
print("+ THIS WILL DELETE THE CURRENT BACKUP!")

deviceip = input("what's the IP of your device?: ")
devicerootpass = input("what's the root password?: ")

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(deviceip, "22", "root", devicerootpass)
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && rm apple-logo-n84@2x~iphone.png && mv ./backup/apple-logo-n84@2x~iphone.png ./')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && rm apple-logo-black-n84@2x~iphone.png && mv ./backup/apple-logo-black-n84@2x~iphone.png ./')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && rm apple-logo-black@2x~iphone.png && mv ./backup/apple-logo-black@2x~iphone.png ./')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && rm apple-logo@2x~iphone.png && mv ./backup/apple-logo@2x~iphone.png ./')
    client.exec_command('cd ../../../System/Library/PrivateFrameworks/ProgressUI.framework && rm -rf backup')
    return client

ssh = createSSHClient(deviceip, "22", "root", devicerootpass)
print("backup folder has been deleted!")
print("restore sucessfully completed!")
