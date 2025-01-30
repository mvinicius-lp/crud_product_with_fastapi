from sqlmodel import Session, select
from models.product import Product
from fastapi import APIRouter, Depends, HTTPException, Query
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

@router.get("/", response_model=list[Product])
def get_product( offset: int = 0, limit: int = Query(default=10, le=100),
                 session: Session = Depends(get_session)):
    return session.exec(select(Product).offset(offset).limit(limit)).all()

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, session: Session = Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product