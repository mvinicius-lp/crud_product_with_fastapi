from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Home"],
)

@router.get("/")
async def root():
    return {"msg": "Bem vindo ao CRUD de produtos"}