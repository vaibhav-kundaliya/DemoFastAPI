from datetime import datetime, timedelta
import jwt
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGO")
JWT_TOKEN_EXPIRY_IN_HOURS = int(os.getenv("JWT_TOKEN_EXPIRY_IN_HOURS"))

def create_access_token(reqData_obj: dict):
    data = dict(reqData_obj)
    expire_time = datetime.utcnow() + timedelta(hours=JWT_TOKEN_EXPIRY_IN_HOURS)
    data['exp_time'] = expire_time.strftime("%Y-%m-%d %H:%M:%S")
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return encoded_jwt

def is_token_expired(token: str):
    decoded_jwt = eval(jwt.decode(token, SECRET_KEY, algorithms='HS256'))
    expired_time = datetime.strptime(decoded_jwt.get("exp"),"%Y-%m-%d %H:%M:%S")
    if expired_time <= datetime.utcnow():
        return True
    return False

def get_email_from_token(token: str):
    decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms='HS256')
    return decoded_jwt.get('email')