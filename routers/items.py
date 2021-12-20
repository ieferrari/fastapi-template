from fastapi import APIRouter
from schemas import items

router = APIRouter()


@router.get("/")
async def get_items():
    return {"msg": "get_items"}


@router.post('/')
async def post_items( item: items.Item, item2: items.ItemBase):
    item_label = item.label
    return {"msg": item_label+str(item.id)}



#class ItemBase(BaseModel):
#    label: str
