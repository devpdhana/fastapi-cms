from pydantic import BaseModel, ConfigDict, Field
import uuid


class Ticket(BaseModel):
    ticket_title: str = Field(min_length=1)
    ticket_description: str
    ticket_type: str


class TicketRequest(Ticket):
    pass


class TicketResponse(Ticket):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    ticket_status: str
