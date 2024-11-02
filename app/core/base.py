from sqlalchemy.ext.declarative import declarative_base
from app.core.registry import model_registry, schema_registry

Base = declarative_base()

def register_model(cls):
    model_registry[cls.__name__] = cls
    return cls

def register_schema(cls):
    schema_registry[cls.__name__] = cls
    return cls
