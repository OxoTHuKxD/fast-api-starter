from typing import Dict
from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def read_dummy(query_param: Optional[str] = None) -> Dict:
    if query_param == "ExceptionTest":
        raise Exception("Test Exception")

    return {"Hello": "World"}
