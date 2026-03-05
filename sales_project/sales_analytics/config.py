import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "sales.db")

FIGURES_DIR = os.path.join(BASE_DIR, "output", "figures")

os.makedirs(FIGURES_DIR, exist_ok=True)