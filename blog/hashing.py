from passlib.context import CryptContext

# Create the password context
pwd_ctxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword():
    def __init__(self, password: str):
        self._password = password
        self._hashed_password = None
        if self._password:
            #  Start with Password Hashing
            self._hashed_password = pwd_ctxt.hash(self._password)
        
                                
    def get_hashed_password(self):
        if self._hashed_password:
            return self._hashed_password
        
 

class UnHashPassword():
    
    def __init__(self, plain_password: str):
        self._plain_password = plain_password
           
    def verify_password(self, hashed_password: str):
        return pwd_ctxt.verify(self._plain_password, hashed_password)
        
        