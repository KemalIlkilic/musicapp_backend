from passlib.context import CryptContext
import bcrypt

""" password_context = CryptContext(
    schemes=['bcrypt']
) """

def generate_password_hash(password : str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')

# Check if the provided password matches the stored password (hashed)
def verify_password(plain_password : str, hashed_password : str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_bytes)




""" def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    return hash

def verify_password(password : str , hash : str) -> bool:
    return password_context.verify(password, hash) """
