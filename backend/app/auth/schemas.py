from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from app.database.db import Base


class SUser(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, pri)