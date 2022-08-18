class User:
    
    def __init__(self, user_id, login, password, status):
        self.id = user_id
        self.login = login
        self.password = password
        self.status = status

    def __str__(self):
        return f"{self.login} ({self.status} permissions)"