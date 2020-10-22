# BIG SPAGHETTI, CODE BE AWARE
# BIG SPAGHETTI, CODE BE AWARE
# BIG SPAGHETTI, CODE BE AWARE
import os
from PIL import Image
import shutil
from zipfile import ZipFile
import paramiko
from scp import SCPClient
from pyfiglet import Figlet
from resizeimage import resizeimage

f = Figlet(font='slant')
print (f.renderText('Kuai - 1.0'))
print("MAKE SURE YOU HAVE A BACKUP DONE BEFORE USING THIS.")
print("IF NOT, BACKUP USING BACKUP.PY!")
print("------------------------------------------------------------")

bootlogofilename = input("what's the filename? (file must be in the same directory): ")
  
shutil.copy(bootlogofilename,"./customlogo/apple-logo-n84@2x~iphone.png")
shutil.copy(bootlogofilename,"./customlogo/apple-logo-black-n84@2x~iphone.png")
shutil.copy(bootlogofilename,"./customlogo/apple-logo-black@2x~iphone.png")
shutil.copy(bootlogofilename,"./customlogo/apple-logo@2x~iphone.png")

with open('./customlogo/apple-logo-n84@2x~iphone.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [300, 300])
        f.close()
        os.remove('./customlogo/apple-logo-n84@2x~iphone.png')
        cover.save('./customlogo/apple-logo-n84@2x~iphone.png', image.format)

with open('./customlogo/apple-logo-black-n84@2x~iphone.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [300, 300])
        f.close()
        os.remove('./customlogo/apple-logo-black-n84@2x~iphone.png')
        cover.save('./customlogo/apple-logo-black-n84@2x~iphone.png', image.format)

with open('./customlogo/apple-logo-black@2x~iphone.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [150, 150])
        f.close()
        os.remove('./customlogo/apple-logo-black@2x~iphone.png')
        cover.save('./customlogo/apple-logo-black@2x~iphone.png', image.format)

with open('./customlogo/apple-logo@2x~iphone.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [150, 150])
        f.close()
        os.remove('./customlogo/apple-logo@2x~iphone.png')
        cover.save('./customlogo/apple-logo@2x~iphone.png', image.format)

print("all images done")        
        
# Upload files to device using SSH

print("time to upload the files to your device!")
deviceip = input("what's the IP of your device?: ")
devicerootpass = input("what's the root password?: ")

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(deviceip, "22", "root", devicerootpass)
    return client

ssh = createSSHClient(deviceip, "22", "root", devicerootpass)
scp = SCPClient(ssh.get_transport())
print("uploading da files")
scp.put('./customlogo/apple-logo-n84@2x~iphone.png', '../../../System/Library/PrivateFrameworks/ProgressUI.framework')
scp.put('./customlogo/apple-logo-black-n84@2x~iphone.png', '../../../System/Library/PrivateFrameworks/ProgressUI.framework')
scp.put('./customlogo/apple-logo@2x~iphone.png', '../../../System/Library/PrivateFrameworks/ProgressUI.framework')
scp.put('./customlogo/apple-logo-black@2x~iphone.png', '../../../System/Library/PrivateFrameworks/ProgressUI.framework')

# Print this if everything done :)
print("everything done")
