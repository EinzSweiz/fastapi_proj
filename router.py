from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix="/task",
    tags=["Tasks"]
)


@router.post("")
async def add_tasks(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {
        "ok": True,
        "task_id": task_id
    }




@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks