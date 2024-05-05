# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, Task as DBTask, Employee as DBEmployee, Device as DBDevice, Project as DBProject, database, create_tables
from schemas import Task, TaskCreate, Employee, Device, Project

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks/", response_model=List[Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(DBTask).all()
    return tasks

@app.get("/employees/", response_model=List[Employee])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(DBEmployee).all()
    return employees

@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.get("/devices/", response_model=List[Device])
def get_devices(db: Session = Depends(get_db)):
    devices = db.query(DBDevice).all()
    return devices

@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(DBDevice).filter(DBDevice.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.get("/projects/", response_model=List[Project])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(DBProject).all()
    return projects

@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(DBProject).filter(DBProject.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = DBTask(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.post("/employees/", response_model=Employee)
async def add_employee(employee: Employee, db: Session = Depends(get_db)):
    new_employee = DBEmployee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@app.post("/devices/", response_model=Device)
async def add_device(device: Device, db: Session = Depends(get_db)):
    new_device = DBDevice(**device.dict())
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

@app.post("/projects/", response_model=Project)
async def create_project(project: Project, db: Session = Depends(get_db)):
    new_project = DBProject(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data_dict = task_data.dict(exclude_unset=True)
    for key, value in task_data_dict.items():
        setattr(task, key, value)
    db.commit()
    return task

@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee: Employee, db: Session = Depends(get_db)):
    emp = db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_data = employee.dict(exclude_unset=True)
    for key, value in emp_data.items():
        setattr(emp, key, value)
    db.commit()
    return emp

@app.put("/devices/{device_id}", response_model=Device)
async def update_device(device_id: int, device: Device, db: Session = Depends(get_db)):
    dev = db.query(DBDevice).filter(DBDevice.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    device_data = device.dict(exclude_unset=True)
    for key, value in device_data.items():
        setattr(dev, key, value)
    db.commit()
    return dev

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: int, project: Project, db: Session = Depends(get_db)):
    existing_project = db.query(DBProject).filter(DBProject.id == project_id).first()
    if not existing_project:
        raise HTTPException(status_code=404, detail="Project not found")
    project_data = project.dict(exclude_unset=True)
    for key, value in project_data.items():
        setattr(existing_project, key, value)
    db.commit()
    return existing_project

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}

@app.delete("/devices/{device_id}")
async def delete_device(device_id: int, db: Session = Depends(get_db)):
    dev = db.query(DBDevice).filter(DBDevice.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(dev)
    db.commit()
    return {"message": "Device deleted"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}

@app.delete("/projects/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    proj = db.query(DBProject).filter(DBProject.id == project_id).first()
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(proj)
    db.commit()
    return {"message": "Project deleted"}
