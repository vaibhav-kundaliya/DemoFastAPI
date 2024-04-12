from passlib.context import CryptContext

cryptcont = CryptContext(schemes=['bcrypt'], deprecated="auto")

def encrypt(plain_text):
    return cryptcont.hash(plain_text)

def compare(plain_text, encrypted_text):
    return cryptcont.verify(plain_text, encrypted_text)