from fastapi import APIRouter, status

from app.package.redis_tools.tools import RedisTools

router = APIRouter(prefix="/api/v1/currency")


@router.get("/{pair}")
def get_currency_pair(pair: str):
    if pair not in [s.encode("utf-8") for s in RedisTools.get_keys()]:
        return {
            "status": status.HTTP_404_NOT_FOUND,
            "error": "This pair doesn't exists",
        }
    return {
        "pair": pair,
        "price": RedisTools.get_pair(pair),
    }
