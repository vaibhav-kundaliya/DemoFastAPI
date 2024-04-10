from passlib.context import CryptContext

cryptcont = CryptContext(schemes=['bcrypt'])

def encrypt(plain_text):
    return cryptcont.hash(plain_text)

def compare(plain_text, encrypted_text):
    return cryptcont.verify(plain_text, encrypted_text)