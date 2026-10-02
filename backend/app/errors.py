"""Standard error responses for the Vendor Quotation Engine API."""

from typing import Any, Optional
<<<<<<< HEAD

=======
>>>>>>> origin/main
from fastapi import HTTPException, status


def not_found(resource: str, resource_id: Any) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "error": "not_found",
            "resource": resource,
            "id": resource_id,
            "message": f"{resource} with id {resource_id} was not found",
        },
    )


<<<<<<< HEAD
def bad_request(
    message: str,
    field: Optional[str] = None
) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "error": "bad_request",
            "field": field,
            "message": message,
        },
=======
def bad_request(message: str, field: Optional[str] = None) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"error": "bad_request", "field": field, "message": message},
>>>>>>> origin/main
    )


def conflict(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
<<<<<<< HEAD
        detail={
            "error": "conflict",
            "message": message,
        },
=======
        detail={"error": "conflict", "message": message},
>>>>>>> origin/main
    )


def unprocessable(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
<<<<<<< HEAD
        detail={
            "error": "unprocessable",
            "message": message,
        },
=======
        detail={"error": "unprocessable", "message": message},
>>>>>>> origin/main
    )