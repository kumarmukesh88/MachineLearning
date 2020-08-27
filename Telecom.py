from cryptography.fernet import Fernet
sim = True
while sim:
    referenceID = input("Enter your Reference ID: ")
    if referenceID.isalnum() and len(referenceID) == 12:
        sim = False
    else:
        print("Incorrect RefernceID!!! ")

key = Fernet.generate_key()
f = Fernet(key)
encodedRefId = f.encrypt(referenceID.encode())
print(encodedRefId)
decodedRefId = f.decrypt(encodedRefId).decode()
print(decodedRefId)


