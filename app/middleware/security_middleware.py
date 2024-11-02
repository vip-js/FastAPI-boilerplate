from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # 添加安全相关的 HTTP 头
        response = await call_next(request)
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        # response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response
