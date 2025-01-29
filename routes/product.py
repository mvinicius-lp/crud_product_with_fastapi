from sqlmodel import Session
from models.product import Product
from fastapi import APIRouter, Depends
from database import get_session


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/", response_model=Product)
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
                   