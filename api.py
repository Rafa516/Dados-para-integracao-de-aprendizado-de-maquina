# api.py
from fastapi import FastAPI
import pandas as pd
import random
from fastapi.responses import JSONResponse

app = FastAPI()

# Função para gerar uma massa de dados grande de estudantes
def generate_student_data(num_students=1000):
    data = {
        'idade': [random.randint(6, 18) for _ in range(num_students)],
        'frequencia': [random.randint(0, 100) for _ in range(num_students)],
        'nota_media': [round(random.uniform(0.0, 10.0), 1) for _ in range(num_students)],
        'distancia_escola': [random.randint(1, 20) for _ in range(num_students)],
        'situacao_socioeconomica': [random.choice(["baixa", "media", "alta"]) for _ in range(num_students)],
    }
    return pd.DataFrame(data)

# Endpoint para retornar uma grande massa de dados em JSON
@app.get("/students/")
def get_students(num_students: int = 1000):
    df = generate_student_data(num_students)
    return JSONResponse(content=df.to_dict(orient="records"))

# Endpoint para retornar um único estudante
@app.get("/student/")
def get_student():
    df = generate_student_data(1)
    return JSONResponse(content=df.to_dict(orient="records")[0])