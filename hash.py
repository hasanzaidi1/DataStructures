import hashlib

# message = "hello"
# sha256 = hashlib.sha256()
# sha256.update(bytes(message,"utf-8"))


# print(sha256.hexdigest())

# print(bytes(message, "utf-8"))

def hash_sha256(byteMessage):
    sha256 = hashlib.sha256()
    sha256.update(byteMessage)
    return sha256.hexdigest()


def read_file_b(file):
    fh = open(file, "rb")
    content = fh.read()
    return content


def hmac(key, data):
    keyData = key + data
    hashValue = hash_sha256(keyData)
    keyHash = key + bytes(hashValue, "utf-8")
    hashValue = hash_sha256(keyHash)
    return hashValue




message = read_file_b("message.txt")
key = read_file_b("key.txt")
print(hash_sha256(message))

print(hmac(key,message))

