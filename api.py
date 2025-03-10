# api.py
from fastapi import FastAPI
import pandas as pd
import random

app = FastAPI()

# Simulando uma massa de dados grande
def generate_student_data(num_students=1000):
    data = {
        'idade': [random.randint(6, 18) for _ in range(num_students)],
        'frequencia': [random.randint(0, 100) for _ in range(num_students)],
        'nota_media': [round(random.uniform(0.0, 10.0), 1) for _ in range(num_students)],
        'distancia_escola': [random.randint(1, 20) for _ in range(num_students)],
        'situacao_socioeconomica': [random.choice(["baixa", "media", "alta"]) for _ in range(num_students)],
    }
    return pd.DataFrame(data)

# Endpoint para obter dados de estudantes
@app.get("/students/")
def get_students(num_students: int = 100):
    df = generate_student_data(num_students)
    return df.to_dict(orient="records")

# Endpoint para obter dados de um único estudante
@app.get("/student/")
def get_student():
    df = generate_student_data(1)
    return df.to_dict(orient="records")[0]