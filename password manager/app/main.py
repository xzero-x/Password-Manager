from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth, database
import uvicorn 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/credentials/", response_model=schemas.Credential)
def create_credential(credential: schemas.CredentialCreate, db: Session = Depends(database.get_db), user_id: int = 1):
    return crud.create_credential(db=db, credential=credential, user_id=user_id)


@app.get("/credentials/", response_model=list[schemas.Credential])
def read_credentials(db: Session = Depends(database.get_db), user_id: int = 1):
    credentials = crud.get_credentials(db, user_id=user_id)
    return credentials

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)