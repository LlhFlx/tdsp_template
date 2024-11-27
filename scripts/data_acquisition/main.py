import pandas as pd
import os

# Mostrar el directorio actual
current_directory = os.getcwd()
print(f"El script se está ejecutando en: {current_directory}")

DATA_PATH = 'data/'
quran = pd.read_csv(f'{DATA_PATH}Quran_english.csv')
old_testament = pd.read_csv(f'{DATA_PATH}Old_Testament_KJ_Bible.csv')

print("> Corán [en inglés]: ")
print(quran.head())


print("> Antiguo Testamento [en inglés]: ")
print(old_testament.head())