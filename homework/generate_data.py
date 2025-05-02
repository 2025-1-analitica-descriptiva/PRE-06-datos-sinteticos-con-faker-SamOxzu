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


if __name__ == "__main__":

    # Generate fake data
    fake_drivers = generate_fake_drivers(100)
    pprint(fake_drivers)