from sqlalchemy.orm import Session
from . import models, schemas, encryption

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = encryption.hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_credential(db: Session, credential: schemas.CredentialCreate, user_id: int):
    encrypted_username = encryption.encrypt_data(credential.username)
    encrypted_password = encryption.encrypt_data(credential.password)
    db_credential = models.Credential(service_name=credential.service_name, encrypted_username=encrypted_username, encrypted_password=encrypted_password, user_id=user_id)
    db.add(db_credential)
    db.commit()
    db.refresh(db_credential)
    return db_credential

def get_credentials(db: Session, user_id: int):
    return db.query(models.Credential).filter(models.Credential.user_id == user_id).all()