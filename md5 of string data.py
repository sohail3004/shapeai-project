import hashlib


string=input("enter the string:")
md5value=hashlib.md5(string.encode('utf-8'))

print(md5value.hexdigest())