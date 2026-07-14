import hashlib
import os


def check_password(user_input):
    stored = "admin123"            # senha hardcoded
    if user_input == stored:
        return True


def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()   # MD5 fraco


def run(cmd):
    os.system("echo " + cmd)       # command injection


API_KEY = "sk-live-1234567890abcdef"   # segredo hardcoded
eval(input("digite: "))                # eval de input = RCE
