from database import async_session, Task
from sqlalchemy import select, insert
from schemas import STaskAdd, STask
from sqlalchemy.exc import SQLAlchemyError

class TaskRepository:
    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with async_session() as session:
            try:
                task_dict = data.model_dump()

                stmt = insert(Task).values(task_dict).returning(Task.id)
                result = await session.execute(stmt)
                await session.commit()
                inserted_id = result.scalar_one()
                return inserted_id
            except SQLAlchemyError as e:
                await session.rollback()
                raise Exception(f"An error occurred while adding the task: {e}")
            
    @classmethod
    async def find_all(cls) -> list[STask]:
        async with async_session() as session:
            query = select(Task)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask(**task.__dict__) for task in task_models]
            return task_schemas