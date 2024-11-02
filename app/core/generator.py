import os
import re
from jinja2 import Environment, FileSystemLoader
from app.core.registry import model_registry

def generate_code():
    env = Environment(loader=FileSystemLoader("app/templates"))
    repository_template = env.get_template("repository.py.j2")
    service_template = env.get_template("service.py.j2")
    route_template = env.get_template("route.py.j2")

    os.makedirs("app/repositories/__generated__", exist_ok=True)
    os.makedirs("app/services/__generated__", exist_ok=True)
    os.makedirs("app/api/__generated__", exist_ok=True)

    for model_name in model_registry:
        print("model_registry", model_name)
        context = {
            "model_name": model_name,
            "model_name_lower": re.sub(r'(?<!^)(?=[A-Z])', '_', model_name).lower()
        }

        # 生成仓储代码
        repository_code = repository_template.render(context)
        repository_file = f"app/repositories/__generated__/{context["model_name_lower"]}_repository.py"
        if not os.path.exists(repository_file):
            with open(repository_file, "w", encoding="utf-8") as f:
                f.write(repository_code)

        # 生成服务代码
        service_code = service_template.render(context)
        service_file = f"app/services/__generated__/{context["model_name_lower"]}_service.py"
        if not os.path.exists(service_file):
            with open(service_file, "w", encoding="utf-8") as f:
                f.write(service_code)

        # 生成路由代码
        route_code = route_template.render(context)
        route_file = f"app/api/__generated__/{context["model_name_lower"]}_route.py"
        if not os.path.exists(route_file):
            with open(route_file, "w", encoding="utf-8") as f:
                f.write(route_code)
