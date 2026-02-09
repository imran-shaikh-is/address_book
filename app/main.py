from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from . import models, schemas, crud, utils
from .logging_config import logger

# todo Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")


# todo Dependency: Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# todo Root endpoint
@app.get("/")
def root():
    return {"message": "Address Book API is running"}


# todo Create address
@app.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db)
):
    logger.info("Creating new address")
    return crud.create_address(db, address)


# todo Get all addresses
@app.get("/addresses/", response_model=list[schemas.AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    logger.info("Fetching all addresses")
    return crud.get_all_addresses(db)


# todo Update address
@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(
    address_id: int,
    address: schemas.AddressUpdate,
    db: Session = Depends(get_db)
):
    logger.info(f"Updating address ID {address_id}")
    updated = crud.update_address(db, address_id, address)

    if not updated:
        logger.error("Address not found")
        raise HTTPException(status_code=404, detail="Address not found")

    return updated


# todo Delete address
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting address ID {address_id}")
    deleted = crud.delete_address(db, address_id)

    if not deleted:
        logger.error("Address not found")
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted successfully"}


# todo Get nearby addresses
@app.get("/addresses/nearby", response_model=list[schemas.AddressResponse])
def get_nearby_addresses(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    distance_km: float = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    logger.info("Fetching nearby addresses")

    addresses = crud.get_all_addresses(db)
    nearby = utils.get_addresses_within_distance(
        addresses, latitude, longitude, distance_km
    )

    return nearby
