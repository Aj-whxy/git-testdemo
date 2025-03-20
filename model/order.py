import enum
from . import Base
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

class OrderStatus(enum.Enum):
    UNPAYED=1
    PAYED=2
    TRANSIT=3
    FINISHED=4
    REFUNDING=5#退款
    REFUNDED=6#已退款

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")
    status = Column(Enum(OrderStatus), nullable=False,default=OrderStatus.UNPAYED)
