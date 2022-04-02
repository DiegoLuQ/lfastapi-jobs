from fastapi import FastAPI
from core.config import settings
from core.db.session import engine
from core.db.base import Base


#https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=create_all#sqlalchemy.schema.MetaData.create_all
def create_tables():
    Base.metadata.create_all(bind=engine)
    
#inicia la aplicacion
def start_application():
    app = FastAPI(title = settings.PROJECT_TITLE, version = settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()


@app.get('/')
def hello_api():
    return {'deatil':'HelloWorld!'}
