from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base


class Face(Base):
    __tablename__ = "faces"

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
    image_url = sa.Column(sa.String, nullable=False)
    confidence = sa.Column(sa.Float, nullable=False)
    x = sa.Column(sa.Float, nullable=False)
    y = sa.Column(sa.Float, nullable=False)
    width = sa.Column(sa.Float, nullable=False)
    height = sa.Column(sa.Float, nullable=False)

    """Relationships"""
    # An alert belongs to a user
    person_id = sa.Column(sa.UUID, sa.ForeignKey("persons.id"))
    person = relationship("Person", back_populates="faces")
