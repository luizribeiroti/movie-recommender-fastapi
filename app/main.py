from fastapi import FastAPI, HTTPException
from app.model import get_recommendations
from app.data_loader import load_data

app = FastAPI(title="MovieLens Recommender API")

movies, ratings = load_data()

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    if user_id not in ratings['userId'].unique():
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    recommendations = get_recommendations(user_id, ratings, movies)
    return {"user_id": user_id, "recommendations": recommendations}