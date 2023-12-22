from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    # For DBStorage
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    # For FileStorage
    @property
    def cities(self):
        return [city for city in storage.all(City).values() if city.state_id == self.id]
