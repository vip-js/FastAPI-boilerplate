import importlib
import pkgutil

def load_models_and_schemas():
    # 加载模型
    import app.models
    for loader, module_name, is_pkg in pkgutil.iter_modules(app.models.__path__):
        importlib.import_module(f"app.models.{module_name}")
    # 加载数据模式
    import app.schemas
    for loader, module_name, is_pkg in pkgutil.iter_modules(app.schemas.__path__):
        importlib.import_module(f"app.schemas.{module_name}")
