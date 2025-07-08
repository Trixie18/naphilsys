import NTRU2

enc = NTRU2.encrypt("test", "Alvin")
dec = NTRU2.decrypt("test", enc)
print("Encrypted message:", enc)
print("Decrypted message:", dec)