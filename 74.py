import hashlib

word = input("Enter a word to be hashed: ")

to_hash = word

to_b = to_hash.encode('utf-8')

hash_md5 = hashlib.md5(to_b).hexdigest()
hash_sha1 = hashlib.sha1(to_b).hexdigest()
hash_sha256 = hashlib.sha256(to_b).hexdigest()
hash_sha512 = hashlib.sha512(to_b).hexdigest()

# Print the resulting hashes
print(f"MD5 hash of '{word}' is: {hash_md5}")
print(f"SHA-1 hash of '{word}' is: {hash_sha1}")
print(f"SHA-256 hash of '{word}' is: {hash_sha256}")
print(f"SHA-512 hash of '{word}' is: {hash_sha512}")