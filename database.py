# database.py para conexión con PostgreSQL.
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

# Actualiza con tus propios detalles de la base de datos PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost:5432/FastAPIDatabase"

# Para conexiones asincrónicas
database = Database(DATABASE_URL)

# Crea el motor SQLAlchemy para PostgreSQL
engine = create_engine(DATABASE_URL)

# Configura sessionmaker para usar con el motor de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base declarativa para tus modelos
Base = declarative_base()

# Definición de modelo para una tarea
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Modelo para empleados
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String)
    email = Column(String)
    phone = Column(String)
    start_date = Column(Date)

# Modelo para dispositivos
class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    brand = Column(String)
    model = Column(String)
    owner = Column(String)
    serial_number = Column(String)
    purchase_date = Column(Date)

# Modelo para proyectos
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lead = Column(String)
    description = Column(String)
    start_date = Column(Date)
    estimated_end_date = Column(Date)

# Función para crear todas las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)

# database.py para Base de Datos en el navegador como SQLite.
"""from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

def create_tables():
    Base.metadata.create_all(bind=engine)
"""