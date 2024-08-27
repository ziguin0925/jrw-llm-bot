from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Base




DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)

#DB에 연결할때는 session메이커로 연결함

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# - autocommit -> 개발자가 직접 db.commit()을 입력해야 데이터 변경
# - autoflush-> db에 데이터를 보내는 것. // 작업을 구분.


# Base.metadata.create_all(bind=engine)

#DB에서 데이터 불러오는거는 java에서 해도 상관없음.

# DB연결하는 함수
def get_db():
    db = SessionLocal()

    try:
        yield db
    except:
        db.close()