import uuid
from enum import Enum

from sqlalchemy import UUID, String, text
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_cms.repositories.schemas.Base import Base


class TicketStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    Done = "Done"


class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    ticket_title: Mapped[str] = mapped_column(String, nullable=False)
    ticket_description: Mapped[str] = mapped_column(String, nullable=False)
    ticket_type: Mapped[str] = mapped_column(String, nullable=False)
    ticket_status: Mapped[TicketStatus] = mapped_column(
        SQLEnum(TicketStatus), nullable=False, server_default=TicketStatus.PENDING.name
    )
