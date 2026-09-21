from fastapi import HTTPException


def not_found(resource: str, resource_id: int):
    return HTTPException(
        status_code=404,
        detail=f"{resource} with id {resource_id} not found"
    )


def conflict(message: str):
    return HTTPException(
        status_code=409,
        detail=message
    )