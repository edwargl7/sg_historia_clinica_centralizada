"""
Settings for clinic_history project.
"""
from database.databases.database_factory import DatabaseFactory


SECRET_KEY = 'mpkYrXRaKv4ntd_KwAVDaKr8qaoAVYJyDW3VR5MPuUJ_majSgnFKN84T4hWReYyZtKdG856M5Ypj3m4xPdgraQ'

DATABASES = {
    'postgres': {
        'database': 'clinic_history',
        'user': 'postgres',
        'password': 'DB2020',
        'host': 'localhost',
        'port': '5432',
    }
}

DB = DatabaseFactory.get_manage_database('postgres', DATABASES['postgres'])
