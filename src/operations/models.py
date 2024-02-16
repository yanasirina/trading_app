from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped, declarative_base
from sqlalchemy import String, Integer, TIMESTAMP


Base = declarative_base()


class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[str] = mapped_column(String, nullable=False)
    figi: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    instrument_type: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(TIMESTAMP)
