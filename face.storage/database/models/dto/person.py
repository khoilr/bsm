from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "persons"

    # Attributes
    id = sa.Column(sa.UUID, primary_key=True, default=uuid4)
    created_at = sa.Column(
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),  # pylint: disable=not-callable
    )
    updated_at = sa.Column(
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),  # pylint: disable=not-callable
        onupdate=sa.func.now,
    )
    name = sa.Column(sa.String, nullable=False)

    """Relationships"""
    # An alert can have many indicators
    faces = relationship("Face", back_populates="persons", cascade="all, delete-orphan")
