from app import app, db
from app.models import Drone

def seed_drone_data():
    with app.app_context():
        drone1 = Drone(name='Drone 1')
        drone2 = Drone(name='Drone 2')

        db.session.add(drone1)
        db.session.add(drone2)

        db.session.commit()

if __name__ == '__main__':
    seed_drone_data()
