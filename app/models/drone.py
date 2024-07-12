from app import db
from app.models.default import Base

class Drone(Base):
    __tablename__ = 'drones'
    name = db.Column(db.String(255))
    
    tasks = db.relationship('Task', backref='drone', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Drone %r>' % (self.id)
    
