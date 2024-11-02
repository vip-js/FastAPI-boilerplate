from fastapi import APIRouter

def include_generated_routes(app):
    import os
    import importlib.util

    router = APIRouter()

    generated_routes_path = os.path.join(os.path.dirname(__file__), "__generated__")
    for file_name in os.listdir(generated_routes_path):
        if file_name.endswith("_route.py"):
            module_name = file_name[:-3]
            spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(generated_routes_path, file_name)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            router.include_router(module.router)

    app.include_router(router)

def include_custom_routes(app):
    # 在此包含自定义的路由
    pass

def include_all_routes(app):
    include_generated_routes(app)
    include_custom_routes(app)

