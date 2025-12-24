import requests
from fastapi import FastAPI

app = FastAPI(title="Advice wrapper")

session = requests.Session()

@app.get("/advice")
def advice():
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    r.raise_for_status()
    data = r.json()

    return {"advice": data["slip"]["advice"]}

@app.get("/advice3")
def advice3():
    advices = []
    for i in range(3):
        response = session.get("https://api.adviceslip.com/advice", timeout=5)
        response.raise_for_status()
        data = response.json()
        advices.append(data["slip"]["advice"])

    return {"advices": advices}

print(advice3())
