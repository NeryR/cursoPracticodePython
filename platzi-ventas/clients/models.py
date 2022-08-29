import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        #Esta funcion global revisar que regresa el método to_dict y se convierte a diccionario
        return vars(self)
    
    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']