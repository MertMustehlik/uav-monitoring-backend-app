from app import db
from app.models.default import Base

class Task(Base):
    __tablename__ = 'tasks'
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    execute_at = db.Column(db.DateTime)
    drone_id = db.Column(db.Integer, db.ForeignKey('drones.id'))

    images = db.relationship('Image', backref='task', lazy=True)

    def __init__(self, name, description, drone_id):
        self.name = name
        self.description = description
        self.drone_id = drone_id

    def __repr__(self):
        return '<Task %r>' % self.id
