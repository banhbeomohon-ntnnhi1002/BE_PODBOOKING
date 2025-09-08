<<<<<<< HEAD
from src.infrastructure.databases.mssql import init_mssql
from src.infrastructure.models import todo_model
=======
from infrastructure.databases.mssql import init_mssql
from infrastructure.models import course_register_model, todo_model, user_model, course_model, consultant_model, appointment_model, program_model, feedback_model,survey_model
>>>>>>> Services_Add-ons

def init_db(app):
    init_mssql(app)
    
<<<<<<< HEAD
from src.infrastructure.databases.mssql import Base
=======
from infrastructure.databases.mssql import Base
>>>>>>> Services_Add-ons
