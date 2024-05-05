from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# Modelo base y de creación para tareas
class TaskBase(BaseModel):
    description: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True

# Modelos para empleados
class EmployeeBase(BaseModel):
    name: str
    position: str
    email: EmailStr
    phone: str
    start_date: Optional[date] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

# Modelos para dispositivos
class DeviceBase(BaseModel):
    type: str
    brand: str
    model: str
    owner: str
    serial_number: str
    purchase_date: Optional[date] = None

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    class Config:
        orm_mode = True

# Modelos para proyectos
class ProjectBase(BaseModel):
    name: str
    lead: str
    description: str
    start_date: date
    estimated_end_date: date

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    class Config:
        orm_mode = True
