from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "17032004"
DB_HOST = "localhost"
DB_PORT = "5434"
DB_NAME = "neurosight"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

)


print("Database connection created successfully")