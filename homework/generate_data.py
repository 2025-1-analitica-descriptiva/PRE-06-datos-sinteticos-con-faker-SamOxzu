import csv
import os
from pprint import pprint

# Importa el objeto Faker desde la librería faker
# para crear data falsa.
from faker import Faker
from tqdm import tqdm  # type: ignore

# Define un objeto Faker para crear data falsa
fake = Faker()

def generate_fake_drivers(n):
    """Generate n fake records.

    Each record has the following fields:
    - driverId: sequential int (unique) beigning in 10
    - name: fake name
    - ssn: fake ssn
    - location: fake address
    - certified: 'Y' or 'N'
    - wage-plan: 'miles' or 'hours'

    """
    # Crea una lista vacía para almacenar los registros
    drivers = []
    # Hace un ciclo for desde 1 hasta n (incluyendo n)
    # Usa tqdm para mostrar una barra de progreso con el nombre de timesheet
    for i in tqdm(range(n), desc="drivers"):
        # Crea un diccionario con los campos de la data falsa
        record = {
            "driverId": i + 10, # Define el id como consecutivo
            # Usa el objeto Faker para crear data falsa
            "name": fake.name(), # Nombre falso
            "ssn": fake.ssn(), # Social Security Number falso
            "location": fake.address(), # Dirección falsa
            # Genera valores aleatorios para los campos 'certified' y 'wage-plan'
            "certified": fake.random_element(elements=("Y", "N")), # Valores posibles: 'Y' o 'N'
            "wage-plan": fake.random_element(elements=("miles", "hours")), # Valores posibles: 'miles' o 'hours'
        }
        # Añade el registro a la lista de drivers
        drivers.append(record)

    return drivers

def generate_fake_timesheet(drivers, n):
    """Generate n fake timesheet records.

    Each record has the following fields:
    - driverId: int (unique)
    - week: int (1-52)
    - hours-logged: int (0, 50-80)
    - miles-logged: int (0-40) * 100

    """
    # Crea una lista vacía para almacenar los registros
    timesheet = []
    # Hace un ciclo for desde 1 hasta n (incluyendo n)
    # Usa tqdm para mostrar una barra de progreso con el nombre de timesheet
    for i in tqdm(range(n), desc="timesheet"):
        # Crea un diccionario con los campos de la data falsa
        record = {
            # Usa el objeto Faker para crear data falsa
            # Genera un id de driver aleatorio de la lista de drivers (solo los que existan)
            "driverId": fake.random_element(elements=drivers)["driverId"],
            # Genera un número aleatorio entre 1 y 52 para la semana
            "week": fake.random_int(min=1, max=52),
            # Genera un número aleatorio entre 50 y 80 para las horas registradas
            "hours-logged": fake.random_int(min=50, max=80),
            # Genera un número aleatorio entre 0 y 40, multiplica por 100 para las millas registradas
            "miles-logged": fake.random_int(min=0, max=40) * 100,
        }
        # Añade el registro a la lista de timesheet
        timesheet.append(record)

    return timesheet

def save_fake_data(fake_data, filename):
    """Save fake data to a CSV file."""

    # Abre el archivo en modo escritura y codificación utf-8
    with open(filename, "w", encoding="utf-8") as f:
        # Usa DictWriter para escribir en el CSV desde el diccionario
        # Define los nombres de las columnas como las claves del primer registro (feildnames)
        writer = csv.DictWriter(f, fieldnames=fake_data[0].keys())
        # Escribe la cabecera del CSV (nombres de las columnas)
        writer.writeheader()
        # Recorre la lista de registros y escribe cada uno en el CSV
        for record in fake_data:
            writer.writerow(record)


if __name__ == "__main__":

    # Genera data falsa
    fake_drivers = generate_fake_drivers(100)
    fake_timesheet = generate_fake_timesheet(fake_drivers, 1000)

    # Crea el directorio "files" si no existe
    if not os.path.exists("files"):
        os.makedirs("files")
    # Guarda la data falsa en archivos CSV
    save_fake_data(fake_drivers, "files/drivers.csv")
    save_fake_data(fake_timesheet, "files/timesheet.csv")

    # Imprime un mensaje de éxito
    print("Data saved to files/")