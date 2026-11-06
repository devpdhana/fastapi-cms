from fastapi_cms.services.iticket_service import ITicketService
from sqlalchemy.orm import Session
from fastapi_cms.repositories.ticket_repository import TicketRepository
from fastapi_cms.dtos.ticket import TicketRequest
from fastapi import status

from fastapi_cms.dtos.api_response import ApiResponse


class TicketService(ITicketService):
    def __init__(self, ticket_repository: TicketRepository):
        self.ticket_repo = ticket_repository
        super().__init__()

    def create_ticket(self, ticket: TicketRequest):
        try:
            result = self.ticket_repo.create_ticket(ticket)
            response = ApiResponse(
                status=status.HTTP_201_CREATED, data=result, message="Ticket created"
            )
            return response
        except Exception as error:
            error_response = ApiResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=None,
                message=str(error),
            )
            return error_response

    def get_all_tickets(self):
        try:
            results = self.ticket_repo.get_all_tickets()
            response = ApiResponse(
                status=status.HTTP_200_OK, data=results, message="Ticket gathered"
            )
            return response
        except Exception as error:
            error_response = ApiResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=None,
                message=str(error),
            )
            return error_response

    def get_ticket_by_id(self, ticket_id):
        try:
            result = self.ticket_repo.get_ticket_by_id(ticket_id=ticket_id)
            if not result:
                return ApiResponse(
                    status=status.HTTP_404_NOT_FOUND,
                    data=None,
                    message="Ticket not found",
                )
            response = ApiResponse(
                status=status.HTTP_200_OK, data=result, message="Ticket created"
            )
            return response
        except Exception as error:
            error_response = ApiResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=None,
                message=str(error),
            )
            return error_response

    def update_ticket(self, ticket_id, ticket):
        try:
            result = self.ticket_repo.update_ticket_by_id(
                ticket_id=ticket_id, ticket=ticket
            )
            if not result:
                return ApiResponse(
                    status=status.HTTP_404_NOT_FOUND,
                    data=None,
                    message="Ticket not found",
                )
            response = ApiResponse(
                status=status.HTTP_200_OK, data=result, message="Ticket created"
            )
            return response
        except Exception as error:
            error_response = ApiResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=None,
                message=str(error),
            )
            return error_response

    def delete_ticket_by_id(self, ticket_id):
        try:
            result = self.ticket_repo.delete_ticket_by_id(ticket_id=ticket_id)
            if not result:
                return ApiResponse(
                    status=status.HTTP_404_NOT_FOUND,
                    data=None,
                    message="Ticket not found",
                )
            return ApiResponse(
                status=status.HTTP_200_OK,
                data=True,
                message="Ticket",
            )
        except Exception as error:
            error_response = ApiResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=None,
                message=str(error),
            )
            return error_response
