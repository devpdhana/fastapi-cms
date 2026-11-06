from sqlalchemy.orm import Session
from fastapi_cms.dtos.ticket import TicketRequest, TicketResponse
from fastapi_cms.repositories.schemas.Ticket import Ticket


class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, ticket: TicketRequest) -> TicketResponse:
        try:
            ticket_result = Ticket(
                ticket_title=ticket.ticket_title,
                ticket_description=ticket.ticket_description,
                ticket_type=ticket.ticket_type,
            )
            self.db.add(ticket_result)
            self.db.commit()
            self.db.refresh(ticket_result)
            ticket_response = TicketResponse.model_validate(ticket_result)
            return ticket_response
        except Exception as error:
            print(error)

    def get_all_tickets(self) -> list[TicketResponse]:
        try:
            results = self.db.query(Ticket).all()
            return [TicketResponse.model_validate(ticket) for ticket in results]
        except Exception as error:
            print(error)

    def get_ticket_by_id(self, ticket_id: str) -> TicketResponse:
        try:
            result = self.db.query(Ticket).filter_by(id=ticket_id).first()
            if not result:
                return None
            return TicketResponse.model_validate(result)
        except Exception as error:
            print(error)

    def update_ticket_by_id(
        self, ticket_id: str, ticket: TicketRequest
    ) -> TicketResponse:
        try:
            result = self.db.query(Ticket).filter_by(id=ticket_id).first()
            result.ticket_title = ticket.ticket_title
            result.ticket_description = ticket.ticket_description
            self.db.commit()
            self.db.refresh(result)
            return TicketResponse.model_validate(result)
        except Exception as error:
            print(error)

    def delete_ticket_by_id(self, ticket_id: str) -> bool:
        try:
            result = self.db.query(Ticket).filter_by(id=ticket_id).delete()
            if not result:
                return False
            self.db.commit()
            self.db.flush()
            return True
        except Exception as error:
            print(error)
            return False
