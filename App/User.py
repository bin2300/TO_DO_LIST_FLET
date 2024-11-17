import sqlite3

class UserManager:
    @staticmethod
    def connect():
        """Retourne une connexion à la base de données SQLite."""
        conn = sqlite3.connect("Data/to_do_list.db")
        return conn

    @staticmethod
    def create_user(id_user, name, email, password):
        """Crée un nouvel utilisateur dans la table User."""
        conn = UserManager.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO User (ID_USER, Name, Email, Password)
                              VALUES (?, ?, ?, ?)''', (id_user, name, email, password))
            conn.commit()
            conn.close()
            print(f"Utilisateur {name} créé avec succès.")
            return 1  # Signal de succès
        except sqlite3.IntegrityError:
            print(f"Erreur : L'utilisateur avec l'ID {id_user} existe déjà.")
            conn.close()
            return 0  # Signal d'erreur

    @staticmethod
    def update_user(id_user, new_name=None, new_email=None, new_password=None):
        """Met à jour le nom, l'email et/ou le mot de passe de l'utilisateur."""
        conn = UserManager.connect()
        cursor = conn.cursor()

        # Met à jour les informations spécifiées
        if new_name:
            cursor.execute('''UPDATE User SET Name = ? WHERE ID_USER = ?''', (new_name, id_user))
        if new_email:
            cursor.execute('''UPDATE User SET Email = ? WHERE ID_USER = ?''', (new_email, id_user))
        if new_password:
            cursor.execute('''UPDATE User SET Password = ? WHERE ID_USER = ?''', (new_password, id_user))

        conn.commit()
        conn.close()
        print(f"Informations de l'utilisateur {id_user} mises à jour.")
        return 1  # Signal de succès

    @staticmethod
    def delete_user(id_user):
        """Supprime un utilisateur de la base de données."""
        conn = UserManager.connect()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM User WHERE ID_USER = ?''', (id_user,))
        conn.commit()
        conn.close()
        print(f"Utilisateur {id_user} supprimé.")
        return 1  # Signal de succès

    @staticmethod
    def delete_all_users():
        """Supprime tous les utilisateurs de la base de données."""
        conn = UserManager.connect()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM User''')
        conn.commit()
        conn.close()
        print("Tous les utilisateurs ont été supprimés.")
        return 1  # Signal de succès

    @staticmethod
    def select_user_by_email_and_password(email, password):
        """Sélectionne un utilisateur par email et mot de passe."""
        conn = UserManager.connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE Email = ? AND Password = ?''', (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            print(f"Utilisateur trouvé : {user}")
            return user  # Retourne toutes les informations de l'utilisateur sous forme de tuple
        else:
            print(f"Aucun utilisateur trouvé avec l'email {email} et le mot de passe donné.")
            return None  # Si aucun utilisateur n'est trouvé

    @staticmethod
    def select_user_by_id(id_user):
        """Sélectionne un utilisateur par ID."""
        conn = UserManager.connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID_USER = ?''', (id_user,))
        user = cursor.fetchone()
        conn.close()

        if user:
            print(f"Utilisateur trouvé : {user}")
            return user  # Retourne toutes les informations de l'utilisateur sous forme de tuple
        else:
            print(f"Aucun utilisateur trouvé avec l'ID {id_user}.")
            return None  # Si aucun utilisateur n'est trouvé
