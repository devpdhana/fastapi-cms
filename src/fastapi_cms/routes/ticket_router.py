from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from fastapi_cms.dtos.ticket import TicketRequest
from fastapi_cms.repositories.db_connect import get_db
from fastapi_cms.repositories.schemas.Ticket import Ticket, TicketStatus
from fastapi_cms.services.ticket_service import TicketService
from fastapi_cms.repositories.ticket_repository import TicketRepository

router = APIRouter(prefix="/ticket")


def get_ticket_service(db):
    repository = TicketRepository(db=db)
    return TicketService(ticket_repository=repository)


@router.get("/health")
def health_check():
    return {"message": "Ticket running successfully"}


@router.post("/")
def create_ticket(data: TicketRequest, db: Session = Depends(get_db)):
    try:
        ticket_service = get_ticket_service(db)
        result = ticket_service.create_ticket(ticket=data)
        return JSONResponse(
            status_code=result.status, content=result.model_dump(mode="json")
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error ${error}"
        )


@router.put("/{ticket_id}")
def update_ticket(ticket_id: str, data: TicketRequest, db: Session = Depends(get_db)):
    try:
        ticket_service = get_ticket_service(db)
        result = ticket_service.update_ticket(ticket_id=ticket_id, ticket=data)
        return JSONResponse(
            status_code=result.status, content=result.model_dump(mode="json")
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error ${error}"
        )


@router.get("/{ticket_id}")
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    try:
        ticket_service = get_ticket_service(db)
        result = ticket_service.get_ticket_by_id(ticket_id=ticket_id)
        return JSONResponse(
            status_code=result.status, content=result.model_dump(mode="json")
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error ${error}"
        )


@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: str, db: Session = Depends(get_db)):
    try:
        ticket_service = get_ticket_service(db)
        result = ticket_service.delete_ticket_by_id(ticket_id=ticket_id)
        return JSONResponse(
            status_code=result.status, content=result.model_dump(mode="json")
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error ${error}"
        )


@router.get("/")
def get_all_tickets(db: Session = Depends(get_db)):
    try:
        ticket_service = get_ticket_service(db)
        result = ticket_service.get_all_tickets()
        return JSONResponse(
            status_code=result.status, content=result.model_dump(mode="json")
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error ${error}"
        )
