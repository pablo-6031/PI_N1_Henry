from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = FastAPI()
app.title = "Aplicacion con FastAPI"

# Cargar el archivo CSV con las películas
movies_df = pd.read_csv("movies_transform.csv")

# Función auxiliar para convertir mes en español a número
def month_to_number(mes):
    """
    Esta función toma un mes en español y lo convierte a su número correspondiente.
    Por ejemplo, 'enero' será convertido a 1, 'febrero' a 2, etc.
    """
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    return meses.get(mes.lower())

# Función auxiliar para convertir día en español a nombre en inglés
def day_to_english(dia):
    """
    Esta función convierte un día de la semana en español a su nombre en inglés.
    Por ejemplo, 'lunes' será convertido a 'Monday', 'martes' a 'Tuesday', etc.
    """
    dias = {
        'lunes': 'Monday', 'martes': 'Tuesday', 'miercoles': 'Wednesday',
        'jueves': 'Thursday', 'viernes': 'Friday', 'sabado': 'Saturday', 'domingo': 'Sunday'
    }
    return dias.get(dia.lower())

# Función que devuelve la cantidad de películas estrenadas en un mes dado
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    """
    Esta función recibe un mes en español y devuelve la cantidad de películas que fueron estrenadas en ese mes
    en la totalidad del dataset. 
    Ejemplo de retorno: "5 películas fueron estrenadas en el mes de enero".
    """
    mes_num = month_to_number(mes)
    if mes_num:
        count = movies_df[pd.to_datetime(movies_df['release_date'], errors='coerce').dt.month == mes_num].shape[0]
        return {"message": f"{count} películas fueron estrenadas en el mes de {mes}"}
    return {"error": "Mes no válido"}

