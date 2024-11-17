import sqlite3

class TaskManager:
    @staticmethod
    def connect():
        """Retourne une connexion à la base de données SQLite."""
        conn = sqlite3.connect("Data/to_do_list.db")
        return conn

    @staticmethod
    def create_task(id_task, id_user, label, date_creation, state="not do"):
        """Crée une nouvelle tâche dans la table Task."""
        if state not in ["do", "not do"]:
            print("Erreur : L'état de la tâche doit être 'do' ou 'not do'.")
            return 0  # Signal d'erreur
        
        conn = TaskManager.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO Task (ID_Task, ID_USER_1, Label, Date_creation, State)
                              VALUES (?, ?, ?, ?, ?)''', (id_task, id_user, label, date_creation, state))
            conn.commit()
            conn.close()
            print(f"Tâche {label} créée avec succès.")
            return 1  # Signal de succès
        except sqlite3.IntegrityError:
            print(f"Erreur : La tâche avec l'ID {id_task} existe déjà.")
            conn.close()
            return 0  # Signal d'erreur

    @staticmethod
    def update_task(id_task, new_label=None, new_state=None, new_date_creation=None):
        """Met à jour le label, l'état et/ou la date de création de la tâche."""
        if new_state and new_state not in ["do", "not do"]:
            print("Erreur : L'état de la tâche doit être 'do' ou 'not do'.")
            return 0  # Signal d'erreur

        conn = TaskManager.connect()
        cursor = conn.cursor()

        # Mise à jour des informations spécifiées
        if new_label:
            cursor.execute('''UPDATE Task SET Label = ? WHERE ID_Task = ?''', (new_label, id_task))
        if new_state:
            cursor.execute('''UPDATE Task SET State = ? WHERE ID_Task = ?''', (new_state, id_task))
        if new_date_creation:
            cursor.execute('''UPDATE Task SET Date_creation = ? WHERE ID_Task = ?''', (new_date_creation, id_task))

        conn.commit()
        conn.close()
        print(f"Tâche {id_task} mise à jour.")
        return 1  # Signal de succès

    @staticmethod
    def delete_task(id_task):
        """Supprime une tâche de la base de données."""
        conn = TaskManager.connect()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Task WHERE ID_Task = ?''', (id_task,))
        conn.commit()
        conn.close()
        print(f"Tâche {id_task} supprimée.")
        return 1  # Signal de succès

    @staticmethod
    def delete_all_tasks():
        """Supprime toutes les tâches de la base de données."""
        conn = TaskManager.connect()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Task''')
        conn.commit()
        conn.close()
        print("Toutes les tâches ont été supprimées.")
        return 1  # Signal de succès

    @staticmethod
    def select_task(id_task):
        """Sélectionne et retourne une tâche en fonction de son ID."""
        conn = TaskManager.connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Task WHERE ID_Task = ?''', (id_task,))
        task = cursor.fetchone()
        conn.close()
        
        if task:
            print(f"Tâche trouvée: {task}")
            return task  # Retourne les informations de la tâche sous forme de tuple
        else:
            print(f"Aucune tâche trouvée avec l'ID {id_task}.")
            return None  # Si aucune tâche n'est trouvée

