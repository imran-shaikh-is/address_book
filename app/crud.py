from sqlalchemy.orm import Session
from . import models, schemas


def create_address(db: Session, address: schemas.AddressCreate):
    new_address = models.Address(
        name=address.name,
        street=address.street,
        city=address.city,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def get_all_addresses(db: Session):
    return db.query(models.Address).all()


def get_address_by_id(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def update_address(db: Session, address_id: int, address: schemas.AddressUpdate):
    db_address = get_address_by_id(db, address_id)

    if not db_address:
        return None

    for field, value in address.dict(exclude_unset=True).items():
        setattr(db_address, field, value)

    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    db_address = get_address_by_id(db, address_id)

    if not db_address:
        return None

    db.delete(db_address)
    db.commit()
    return db_address
