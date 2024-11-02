from typing import TypeVar, Generic, List, Dict, Any, Optional
from app.repositories.base import BaseRepository

# 定义一个泛型类型 T，用于表示模型类型
T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    async def create(self, **kwargs) -> Dict[str, Any]:
        """创建一条记录并返回其字典格式"""
        return await self.repository.create(**kwargs)

    async def get_by_id(self, id: Any) -> Optional[Dict[str, Any]]:
        """根据 ID 获取记录并返回其字典格式"""
        return await self.repository.get_by_id(id)

    async def update(self, id: Any, **kwargs) -> Optional[Dict[str, Any]]:
        """根据 ID 更新记录并返回更新后的字典格式"""
        return await self.repository.update(id, **kwargs)

    async def delete(self, id: Any) -> bool:
        """根据 ID 删除记录，返回操作结果"""
        return await self.repository.delete(id)

    async def get_all(self) -> List[Dict[str, Any]]:
        """获取所有记录并返回字典列表"""
        return await self.repository.get_all()

    async def get_all_paginated(self, page: int = 1, page_size: int = 10) -> List[Dict[str, Any]]:
        """分页获取记录并返回字典列表"""
        return await self.repository.get_all_paginated(page, page_size)

    async def select_by_condition(
        self, conditions: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """根据动态条件查询记录并返回字典列表"""
        return await self.repository.select_by_condition(conditions)

    async def select_by_condition_paginated(
        self,
        conditions: Dict[str, Any],
        page: int = 1,
        page_size: int = 10,
        order_by: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        """根据动态条件分页查询记录并返回字典列表"""
        return await self.repository.select_by_condition_paginated(conditions, page, page_size, order_by)

