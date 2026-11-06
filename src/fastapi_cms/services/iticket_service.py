from abc import ABC, abstractmethod

from fastapi_cms.dtos.ticket import TicketRequest


class ITicketService(ABC):
    @abstractmethod
    def get_all_tickets():
        pass

    @abstractmethod
    def get_ticket_by_id(ticket_id: str):
        pass

    @abstractmethod
    def create_ticket(ticket: TicketRequest):
        pass

    @abstractmethod
    def update_ticket(ticket_id: str, ticket: TicketRequest):
        pass

    @abstractmethod
    def delete_ticket_by_id(ticket_id: str):
        pass
