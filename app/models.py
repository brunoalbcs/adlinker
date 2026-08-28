from sqlalchemy import Column, String, Integer
from app.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    link_original = Column(String, nullable=False)
    link_curto = Column(String, unique=True, index=True, nullable=False)