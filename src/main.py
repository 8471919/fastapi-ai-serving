# fastapi라이브러리에서 FastAPI를 불러온다.
from fastapi import FastAPI
from src.routers.house import house_router

# FastAPI 함수를 실행시키면, Fastapi 서버가 열리는데,
# 그 서버를 app이라는 변수에 담겠다.
app = FastAPI()

# /house 라는 경로를 타면 house_router로 가게끔 길을 붙여준다.
app.include_router(house_router, prefix="/house")

# @는 데코레이터 라고 부른다. 꾸며주는 아이. 
# 함수나 클래스, 변수 등을 꾸며주는 역할
# 
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
def getUser():
  return {"name": "hansu", "age":28 }

# HTTP 5개
# GET(read), POST(create)
# # PUT(update), PATCH(update) 
# DELETE(delete)