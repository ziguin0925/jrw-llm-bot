#DB 조작(DB와 소통).

from sqlalchemy.orm import Session
from model import Item
from datetime import datetime

def create_item(db:Session, name:str, price:int, stock:int):
    new_item = Item(name=name, price=price, stock=stock, created_at=datetime.now)

    db.add(new_item)
    db.commit()

    return new_item

def get_item(db:Session, item_id = int):
    item = db.query(Item).filter(item_id == item_id).first()

    return item


def get_all_items(db: Session):
    items = db.query(Item).all()

    return items

def update_item(db:Session, item_id:int, name:str=None, price:int=None, stock:int=None):
    item = get_item(db, item_id)
    
    if item is None:
        return None
    
    if name is not None:
        item.name=name
    if price is not None:
        item.price=price
    if stock is not None:
        item.stock=stock
    
    db.commit()
    return item

def delete_item(db:Session, item_id:int):
    item=get_item(db, item_id)

    db.delete(item)
    db.commit()

    return item


#Django는 더 쉽다.

# + Authentication -> JWT Auth

# AWS Lambda (Serverless 백엔드 구축 가능)

# 백엔드에 자바를 왜 쓰는지? -> 파이썬보다 빠른 속도때문 => 세상의 기기 자체들의 속도는 계속해서 빨라지고 있음
# 요즘에는 기기성능이 좋아서 
# 옜날에는 파이썬이 느려서 안썼는데 하드웨어(컴퓨팅 파워)가 좋아지다 보니 쓸만해서 파이썬을 사용하게 됨.


