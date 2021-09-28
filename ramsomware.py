from ency import Decrypt, Encrypt
import sys
if(len(sys.argv) > 1):
    Decrypt(sys.argv[1])
else:
    Encrypt()