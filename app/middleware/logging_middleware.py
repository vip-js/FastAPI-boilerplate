import logging
import uuid
import time
import os
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


# 确保日志目录存在
log_file_path = "logs/app.log"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# 配置日志记录
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 为每个请求生成唯一的请求ID
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        start_time = time.time()
        logger.info(f"请求 {request.method} {request.url}")
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"响应 {response.status_code} 耗时 {process_time} 秒")
        return response
