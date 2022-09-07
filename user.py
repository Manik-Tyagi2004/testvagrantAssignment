class User:
    
    def __init__(self, name, phone_no, is_admin = False):
        self.name = name 
        self.phone_no = phone_no 
        self.isadmin = is_admin
        
    def isAdmin(self):
        return self.is_admin