from sqlmodel import SQLModel, Field
from datetime import datetime

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    date_fab: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date_val: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    cod: int 