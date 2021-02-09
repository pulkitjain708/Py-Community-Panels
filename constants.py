from enum import Enum

class UserTypes(Enum): 
    SA = "Super Admin"
    A = "Admin"
    U = "User"
    
class Status(Enum):
    f="Pending"
    t="Confirmed"

class LoginStatus(Enum):
    t="Logged"
    f="Not Logged"

class Activation(Enum):
    t="Activated"
    f="Deactivated"

class Gender(Enum):
    m="Male"
    f="Female"