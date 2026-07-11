from sqlalchemy import (
    Integer,
    String,
    Float,
    BigInteger,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)

from datetime import datetime


class Base(DeclarativeBase):
    pass



class Goal(Base):

    __tablename__ = "goals"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    title: Mapped[str] = mapped_column(
        String(100)
    )


    target_amount: Mapped[float] = mapped_column(
        Float
    )


    current_amount: Mapped[float] = mapped_column(
        Float,
        default=0
    )


    deadline: Mapped[str] = mapped_column(
        String(20)
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    transactions = relationship(
        "Transaction",
        back_populates="goal",
        cascade="all, delete"
    )



class Transaction(Base):

    __tablename__ = "transactions"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    goal_id: Mapped[int] = mapped_column(
        ForeignKey("goals.id")
    )


    amount: Mapped[float] = mapped_column(
        Float
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    goal = relationship(
        "Goal",
        back_populates="transactions"
    )



class UserSettings(Base):

    __tablename__ = "settings"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True
    )


    reminders: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )