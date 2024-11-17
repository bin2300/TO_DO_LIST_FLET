import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="to_do_list.db", data_folder="Data"):
        self.db_name = db_name
        self.data_folder = data_folder
        self.db_path = os.path.join(self.data_folder, self.db_name)
        self.create_data_folder()
        self.create_database()

    def create_data_folder(self):
        # Vérifie si le dossier "Data" existe, sinon il le crée
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            print(f"Dossier {self.data_folder} créé.")

    def create_database(self):
        # Crée la base de données si elle n'existe pas
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            print(f"Base de données {self.db_name} créée.")

            # Création des tables si elles n'existent pas déjà
            cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                                ID_USER TEXT PRIMARY KEY,
                                Name TEXT,
                                Email TEXT,
                                Password TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
                                ID_Task TEXT PRIMARY KEY,
                                ID_USER_1 TEXT,
                                Label TEXT,
                                Date_creation TEXT,
                                State TEXT,
                                FOREIGN KEY (ID_USER_1) REFERENCES User(ID_USER))''')

            conn.commit()
            conn.close()
            print("Tables créées ou déjà existantes.")
        else:
            print(f"Base de données {self.db_name} existe déjà.")

    def connect(self):
        # Connexion à la base de données SQLite
        return sqlite3.connect(self.db_path)

# Utilisation de la classe
db_manager = DatabaseManager()

# Vous pouvez maintenant utiliser db_manager.connect() pour obtenir une connexion à la base de données.
