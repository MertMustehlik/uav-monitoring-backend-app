from app import app, db
from app.models.drone import Drone
from app.models.user import User

def create_tables():
    with app.app_context():
        db.create_all()

def seed_user_data():
    with app.app_context():
        email = "admin@admin.com"
        password = "123123"

        user = User(email=email, password="")
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

def seed_drone_data():
    with app.app_context():
        drone1 = Drone(name='Drone 1')
        drone2 = Drone(name='Drone 2')

        db.session.add(drone1)
        db.session.add(drone2)

        db.session.commit()

if __name__ == '__main__':
    create_tables()  # Tabloları oluştur
    seed_drone_data()
    seed_user_data()
