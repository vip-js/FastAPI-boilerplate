from fastapi import FastAPI
from app.core.loader import load_models_and_schemas
from app.core.generator import generate_code
from app.api import include_all_routes
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.security_middleware import SecurityMiddleware
from app.containers import Container
from app.core.plugin_loader import load_plugins

def create_app() -> FastAPI:
    # 创建 FastAPI 实例
    app = FastAPI()
    
    # 设置依赖注入容器
    app.container = Container()

    # 加载模型和数据模式
    load_models_and_schemas()
    
    # 自动生成代码
    generate_code()
    
    # 加载插件
    load_plugins(app)
    
    # 注册路由
    include_all_routes(app)
    
    # 添加中间件
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(SecurityMiddleware)
    
    return app

app = create_app()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI-boilerplate!"}


