from typing import Type, TypeVar, Generic, List, Optional, Dict, Any
from sqlalchemy import select, update, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

# 定义一个泛型类型 T，用于表示模型类型
T = TypeVar('T', bound=DeclarativeMeta)

class BaseRepository(Generic[T]):
    def __init__(self, db_session: AsyncSession, model: Type[T]):
        self.db = db_session
        self.model = model  # 子类可以设置具体的模型类        

    async def create(self, **kwargs) -> T:
        """创建一条记录并返回模型实例"""
        instance = self.model(**kwargs)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def get_by_id(self, id: Any) -> Optional[T]:
        """根据 ID 获取记录"""
        stmt = select(self.model).where(self.model.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, id: Any, **kwargs) -> Optional[T]:
        """根据 ID 更新记录并返回模型实例"""
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**kwargs)
            .returning(self.model)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete(self, id: Any) -> bool:
        """根据 ID 删除记录"""
        stmt = delete(self.model).where(self.model.id == id)
        await self.db.execute(stmt)
        await self.db.commit()
        return True

    async def get_all(self) -> List[T]:
        """获取所有记录"""
        stmt = select(self.model)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_all_paginated(self, page: int = 1, page_size: int = 10) -> List[T]:
        """分页获取记录"""
        offset = (page - 1) * page_size
        stmt = select(self.model).offset(offset).limit(page_size)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def select_by_condition(self, conditions: Dict[str, Any]) -> List[T]:
        """根据动态条件查询记录"""
        stmt = select(self.model)
        filters = [
            getattr(self.model, field) == value
            for field, value in conditions.items()
            if hasattr(self.model, field)
        ]
        if filters:
            stmt = stmt.where(and_(*filters))
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def select_by_condition_paginated(
        self,
        conditions: Dict[str, Any],
        page: int = 1,
        page_size: int = 10,
        order_by: Optional[Any] = None,
    ) -> List[T]:
        """根据动态条件分页查询记录"""
        offset = (page - 1) * page_size
        stmt = select(self.model).offset(offset).limit(page_size)
        filters = [
            getattr(self.model, field) == value
            for field, value in conditions.items()
            if hasattr(self.model, field)
        ]
        if filters:
            stmt = stmt.where(and_(*filters))
        if order_by is not None:
            stmt = stmt.order_by(order_by)    
        result = await self.db.execute(stmt)
        return result.scalars().all()

