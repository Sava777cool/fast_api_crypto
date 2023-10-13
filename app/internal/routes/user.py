from fastapi import APIRouter, status

router = APIRouter(prefix="/api/v1")


@router.get("/user")
def get_users():
    return {
        "status": status.HTTP_200_OK,
        "message": "It is work",
    }
