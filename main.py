from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from models import Pokemon

Base.metadata.create_all(bind=engine) #Créer les tables si elles n'existent pas.

app = FastAPI()

@app.get("/")
def read_root():
    return {"Bienvenue sur l'API Pokemon"}

@app.get("/pokemon/{item_id}")
def read_pokemon(item_id: int, db: Session = Depends(get_db)):
    pokemon = db.query(Pokemon).filter(Pokemon.id == item_id).first()
    if pokemon:
        return pokemon
    else:
        raise HTTPException(status_code=404, detail="Pokemon not found")

@app.post("/pokemon")
def create_pokemon(pokemon: dict, db: Session = Depends(get_db)):
    db_pokemon = Pokemon(**pokemon)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

@app.put("/pokemon/{item_id}")
def update_pokemon(item_id: int, pokemon: dict, db: Session = Depends(get_db)):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == item_id).first()
    if db_pokemon:
        for key, value in pokemon.items():
            setattr(db_pokemon, key, value)
        db.commit()
        db.refresh(db_pokemon)
        return db_pokemon
    else:
        raise HTTPException(status_code=404, detail="Pokemon not found")

@app.delete("/pokemon/{item_id}")
def delete_pokemon(item_id: int, db: Session = Depends(get_db)):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == item_id).first()
    if db_pokemon:
        db.delete(db_pokemon)
        db.commit()
        return {"message": "Pokemon deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Pokemon not found")