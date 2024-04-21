from fastapi import APIRouter
from src.services.house import run_model

# 길을 붙여주는 애를 house_router랑 router 변수에 담을거다.
house_router = router = APIRouter()

# /house/price/predict 로 Get요청이 들어오면 실행
@router.get('/price/predict')
async def get_prediction_of_house_price(criminal: float, room: float):
  price = run_model(criminal, room)
  return price
  
# /house 로 GET 요청이 들어오면 실행
@router.get("/")
async def getHouse():
  return "House"
