# FastAPI-boilerplate

一个基于 **FastAPI** 和 **SQLAlchemy 2.x** 的自动化框架，旨在让开发者只需编写业务逻辑代码，其余部分由框架自动完成。框架集成了性能优化和安全机制，代码优雅简洁，遵循高内聚、低耦合、易扩展的设计原则。

## 项目简介

本项目旨在提供一个高度自动化的后端框架，开发者只需关注业务逻辑的实现，其余部分如路由、服务、仓储等代码由框架自动生成。框架内置了性能优化和安全机制，适用于构建高性能、高可用的 Web 应用程序。

## 特性

- **自动化代码生成**：根据模型和数据模式，自动生成仓储、服务和路由代码。
- **依赖注入**：使用 `dependency-injector`，自动管理依赖关系。
- **安全性**：内置数据验证、密码加密、认证与授权、防止 SQL 注入、安全头设置等功能。
- **高性能**：采用异步编程、连接池优化、缓存机制、数据库索引优化，支持横向扩展。
- **防御攻击**：通过限流、防暴力破解、输入验证等手段，增强系统的防御能力。
- **日志记录**：标准化日志、请求响应日志、异常日志、日志切割、日志聚合，便于问题的定位和解决。
- **可扩展性**：遵循高内聚、低耦合的设计原则，易于维护和扩展。

## 技术栈

- **后端框架**：FastAPI
- **数据库**：PostgreSQL
- **ORM**：SQLAlchemy 2.x
- **异步编程**：asyncio
- **依赖注入**：dependency-injector
- **缓存扩展**：redis
- **消息队列**：可扩展集成（如 RabbitMQ、Kafka）
- **模板引擎**：Jinja2

## 项目结构

```
FastAPI-boilerplate/
├── app/
│   ├── __init__.py                   # 标识 app 目录为包
│   ├── main.py                       # 应用入口
│   ├── config.py                     # 配置文件
│   ├── database.py                   # 数据库连接
│   ├── containers.py                 # 依赖注入容器
│   ├── core/                         # 核心模块
│   │   ├── __init__.py
│   │   ├── base.py                   # 基础模型与服务
│   │   ├── generator.py              # 自动代码生成器
│   │   ├── loader.py                 # 模块自动加载器
│   │   ├── plugin_loader.py          # 插件加载器
│   │   └── registry.py               # 注册表
│   ├── models/                       # 数据库模型
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/                      # Pydantic 数据模式
│   │   ├── __init__.py
│   │   └── user.py
│   ├── repositories/                 # 仓储层
│   │   ├── __init__.py
│   │   ├── base.py                   # 仓储基类
│   │   └── __generated__/            # 自动生成的仓储代码
│   │       ├── __init__.py
│   │       └── user_repository.py
│   ├── services/                     # 服务层
│   │   ├── __init__.py
│   │   ├── base.py                   # 服务基类
│   │   └── __generated__/            # 自动生成的服务代码
│   │       ├── __init__.py
│   │       └── user_service.py
│   ├── api/                          # API 路由
│   │   ├── __init__.py
│   │   ├── base.py                   # 路由基类
│   │   └── __generated__/            # 自动生成的路由代码
│   │       ├── __init__.py
│   │       └── user_route.py
│   ├── utils/                        # 工具模块
│   │   ├── __init__.py
│   │   ├── security.py               # 安全相关（如密码加密）
│   │   └── query_helpers.py          # 查询帮助工具
│   ├── middleware/                   # 中间件
│   │   ├── __init__.py
│   │   ├── security_middleware.py    # 安全中间件
│   │   └── logging_middleware.py     # 日志中间件
│   ├── templates/                    # 代码生成模板
│   │   ├── repository.py.j2
│   │   ├── service.py.j2
│   │   └── route.py.j2
│   ├── plugins/                      # 插件目录
│   │   └── __init__.py
│   └── requirements.txt              # 项目依赖
├── init_db.py                        # 数据库初始化脚本
└── .env                              # 环境变量配置
```

## 环境要求

- Python 3.8 及以上版本
- PostgreSQL 数据库
- Redis 缓存（可选，用于缓存和限流）
- 操作系统：Windows、macOS、Linux

## 安装与运行

### 克隆仓库

```
bash
git clone https://github.com/vip-js/FastAPI-boilerplate.git
cd FastAPI-boilerplate
```

### 创建虚拟环境

```
bash

python3 -m venv venv
source venv/bin/activate  # 对于Linux/Mac
venv\Scripts\activate     # 对于Windows
```

### 安装依赖

```
bash

pip install -r requirements.txt
```

### 配置环境变量

根据 `app/config.py`，您可以通过环境变量或在 `.env` 文件中设置以下配置：

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `SECRET_KEY`
- `REDIS_HOST`
- `REDIS_PORT`

示例 `.env` 文件：

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=yourdatabase
SECRET_KEY=your_secret_key
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 初始化数据库

运行数据库初始化脚本：

```
bash

python init_db.py
```

### 启动应用

```
bash

uvicorn app.main:app --reload
```

应用将运行在 `http://127.0.0.1:8000`。

## 使用说明

### 添加新模型

1. **编写模型**

   在 `app/models/` 目录下创建新的模型文件，例如 `product.py`：

   ```
   python
   
   
   复制代码
   from sqlalchemy import Column, Integer, String, Float
   from app.core.base import Base, register_model
   
   @register_model
   class Product(Base):
       __tablename__ = 'products'
   
       id = Column(Integer, primary_key=True, index=True)
       name = Column(String(length=100), nullable=False)
       price = Column(Float, nullable=False)
   ```

2. **编写数据模式**

   在 `app/schemas/` 目录下创建对应的数据模式文件，例如 `product.py`：

   ```
   python
   
   from pydantic import BaseModel, Field
   from app.core.base import register_schema
   
   @register_schema
   class ProductBase(BaseModel):
       name: str = Field(..., min_length=1, max_length=100)
       price: float
   
   @register_schema
   class ProductCreate(ProductBase):
       pass
   
   @register_schema
   class ProductRead(ProductBase):
       id: int
   
       class Config:
           orm_mode = True
   ```

3. **运行应用**

   重启应用，框架将自动生成仓储、服务和路由代码。

### 编写业务逻辑

- **服务层逻辑**

  如果需要自定义业务逻辑，可以在生成的服务类中添加或重写方法。

- **路由**

  框架自动注册了基本的 CRUD 路由，您也可以手动添加新的路由。

## 性能与安全

- **异步编程**：全程采用异步编程，充分利用 FastAPI 和 SQLAlchemy 的异步特性。
- **连接池优化**：调整数据库连接池参数，提高并发性能。
- **缓存机制**：集成 Redis，实现缓存和限流功能。
- **安全性**：内置数据验证、密码哈希、JWT 认证、权限控制等。
- **防御攻击**：通过限流中间件、防止 SQL 注入和 XSS 攻击等手段，增强安全性。

## 日志与监控

- **日志记录**：使用 Python 的 `logging` 模块，记录请求、响应和异常信息。
- **日志切割**：支持日志文件按日期或大小切割，便于管理。
- **性能监控**：集成 Prometheus，用于监控应用的性能指标。
- **错误报警**：可扩展添加错误报警功能，如邮件、短信通知等。

## 常见问题

1. **数据库连接失败**
   - 请检查 `config.py` 中的数据库配置是否正确。
   - 确保 PostgreSQL 服务已启动。
2. **无法生成代码**
   - 确保在添加新模型和数据模式后，重启应用以触发代码生成器。
3. **依赖包版本兼容性问题**
   - 请确保使用 `requirements.txt` 中指定的版本安装依赖。

## 贡献指南

欢迎提交问题（Issue）和合并请求（Pull Request）来改进本项目。在提交前，请确保遵循以下准则：

- 确保代码风格一致，变量命名清晰。
- 添加必要的注释，说明代码逻辑。
- 提交前进行充分的测试，确保代码稳定。

## 许可证

MIT 许可证。

------

感谢您使用本项目！如果您有任何问题或建议，欢迎提出。