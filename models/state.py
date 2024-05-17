#!/usr/bin/python3
"""
State class for creating State table
#!/Users/mistarkelly/vagrant_project/My-Projects/ALX-ONLY/AirBnB_clone_v2/.venv/bin/python3

"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City


class State(BaseModel, Base):
    """
         state table.
         would be a Table in the database.
     """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    
    @property
    def cities(self):
        """
            Getter method for cities
            Returns a list of City objects linked to the current State
        """
        from models import storage
        cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
