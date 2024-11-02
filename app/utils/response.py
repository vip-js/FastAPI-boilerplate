from typing import TypeVar, Generic, Optional
from fastapi import status
from pydantic import BaseModel

# 定义一个泛型类型，用于指定数据类型
T = TypeVar("T")

# 使用泛型类来创建标准响应模型
class ResponseModel(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

# 定义响应包装函数
def create_response(data: T = None, code: int = status.HTTP_200_OK, message: str = "success") -> ResponseModel[T]:
    return ResponseModel[T](code=code, message=message, data=data)

def error_response(message: str = "An error occurred", code: int = status.HTTP_500_INTERNAL_SERVER_ERROR) -> ResponseModel[None]:
    return ResponseModel(code=code, message=message, data=None)

