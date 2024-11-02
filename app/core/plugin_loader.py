import importlib
import pkgutil

def load_plugins(app):
    import app.plugins
    for module_name in pkgutil.iter_modules(app.plugins.__path__):
        module = importlib.import_module(f"app.plugins.{module_name}")
        if hasattr(module, "register_plugin"):
            module.register_plugin(app)
