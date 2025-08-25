from src.infrastructure.databases.mssql import init_mssql
from src.infrastructure.models import todo_model

def init_db(app):
    init_mssql(app)
    
from src.infrastructure.databases.mssql import Base