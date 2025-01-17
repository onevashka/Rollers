from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base
from datetime import datetime


class SCategory(Base):

    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, 
                                    autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class SProduct(Base):

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    time_reg: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id'))
