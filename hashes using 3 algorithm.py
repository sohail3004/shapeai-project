import hashlib

# UTF-8 encoding
message = "Some text to hash".encode()
print("MD5:", hashlib.md5(message).hexdigest())

# hash with SHA-2 (SHA-256 & SHA-512)
str1="hashing".encode()
print("SHA-256:", hashlib.sha256(str1).hexdigest())

print("SHA-512:", hashlib.sha512(str1).hexdigest())


# hash with SHA-3
str2="python".encode()
print("SHA-3-256:", hashlib.sha3_256(str2).hexdigest())

print("SHA-3-512:", hashlib.sha3_512(str2).hexdigest())


# 256-bit BLAKE2s
str3="netwrok".encode()
print("BLAKE2c:", hashlib.blake2s(str3).hexdigest())
# 512-bit BLAKE2b
print("BLAKE2b:", hashlib.blake2b(str3).hexdigest())