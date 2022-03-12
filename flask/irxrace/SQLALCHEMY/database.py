from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/irxrace')
Session = sessionmaker(bind=engine)
Base = declarative_base()



class races(Base):
    __tablename__ = "races"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    starting_position = Column(String, nullable=False)
    ending_position = Column(String, nullable=False)
    qualifying_time = Column(String, nullable=False)
    average_lap_times = Column(String, nullable=False)
    best_lap_time = Column(String, nullable=False)
    

# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'starting position': '1', 'ending position': '1', 'qualifying time': '28.674', 'average lap times': '30.004', 'best lap time': '28.794'},
    {'starting position': '4', 'ending position': '2', 'qualifying time': '28.736', 'average lap times': '30.072', 'best lap time': '28.758'},
    {'starting position': '5', 'ending position': '3', 'qualifying time': '28.763', 'average lap times': '30.161', 'best lap time': '28.990'},
    {'starting position': '3', 'ending position': '4', 'qualifying time': '28.793', 'average lap times': '30.167', 'best lap time': '29.161'},
    {'starting position': '2', 'ending position': '5', 'qualifying time': '28.844', 'average lap times': '30.223', 'best lap time': '28.784'},
    {'starting position': '8', 'ending position': '6', 'qualifying time': '28.898', 'average lap times': '30.335', 'best lap time': '29.220'},
    {'starting position': '16', 'ending position': '7', 'qualifying time': '28.925', 'average lap times': '30.592', 'best lap time': '29.281'},
    {'starting position': '22', 'ending position': '8', 'qualifying time': '28.942', 'average lap times': '30.625', 'best lap time': '29.452'},
    {'starting position': '19', 'ending position': '9', 'qualifying time': '29.027', 'average lap times': '30.684', 'best lap time': '29.046'},
    {'starting position': '12', 'ending position': '10', 'qualifying time': '29.049', 'average lap times': '30.839', 'best lap time': '28.906'},
    {'starting position': '20', 'ending position': '11', 'qualifying time': '29.145', 'average lap times': '31.016', 'best lap time': '29.504'},
    {'starting position': '21', 'ending position': '12', 'qualifying time': '29.242', 'average lap times': '31.351', 'best lap time': '29.377'},
    {'starting position': '18', 'ending position': '13', 'qualifying time': '29.294', 'average lap times': '31.677', 'best lap time': '29.649'},
    {'starting position': '7', 'ending position': '14', 'qualifying time': '29.429', 'average lap times': '31.845', 'best lap time': '29.307'},
    {'starting position': '17', 'ending position': '15', 'qualifying time': '29.571', 'average lap times': '32.182', 'best lap time': '29.812'},
]

# Turn the seed data into a list of races objects
races_objects = []
for item in seed_data:
    v = races(starting_position=item["starting position"], ending_position=item["ending position"], qualifying_time=item["qualifying time"], average_lap_times=item["average lap times"], best_lap_time=item["best lap time"])
    races_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(races_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# SELECT * FROM races
races = session.query(races).all()

print('INSERTED races:', races)
print('')  # separator

for v in races:
    print(v.starting_position, v.ending_position, v.qualifying_time, v.average_lap_times, v.best_lap_time)

print('')  # separator

# SELECT * FROM races ORDER BY name, color
races = session.query(races).order_by(
    races.starting_position, races.ending_position, races.qualifying_time, races.average_lap_times, races.best_lap_time).all()

for i, v in enumerate(races):
    print(str(i+1) + ". " + v.formatted_name())

# ... rest of model definition

    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()



###################################################

class incidents(Base):
    __tablename__ = "incidents"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    cars_involved = Column(String, nullable=False)
    number_of_incidents = Column(String, nullable=False)



# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '2', 'number of incidents': '2'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '1', 'number of incidents': '2'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '2', 'number of incidents': '4'},
    {'cars involved': '3', 'number of incidents': '8'},
    {'cars involved': '4', 'number of incidents': '8'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '0', 'number of incidents': '0'},
    {'cars involved': '3', 'number of incidents': '4'},
    {'cars involved': '6', 'number of incidents': '9'},
]

# Turn the seed data into a list of incidents objects
incidents_objects = []
for item in seed_data:
    v = incidents(cars_involved=item["cars involved"],  number_of_incidents=item["number of incidents"])
    incidents_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(incidents_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# SELECT * FROM incidents
incidents = session.query(incidents).all()

print('INSERTED incidents:', incidents)
print('')  # separator

for v in incidents:
    print(v.number_of_incidents, v.cars_involved)

print('')  # separator

# SELECT * FROM incidents ORDER BY name, color
incidents = session.query(incidents).order_by(
    incidents.number_of_incidents, incidents.cars_involved).all()

for i, v in enumerate(incidents):
    print(str(i+1) + ". " + v.formatted_name())

# ... rest of model definition

    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()





################################################

class Drivers(Base):
    __tablename__ = "Drivers"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email_address = Column(String, nullable=False)



# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'name': 'Joe Backus', 'password': '12345', 'email address': ''},
    {'name': 'William Vining', 'password': '51234', 'email address': ''},
    {'name': 'Nahuel Diaz Caviglia', 'password': '61235', 'email address': ''},
    {'name': 'Andy Wilkinson', 'password': '53116', 'email address': ''},
    {'name': 'William Miller', 'password': '123567', 'email address': ''},
    {'name': 'Nathan Stevens', 'password': '09843', 'email address': ''},
    {'name': 'Dylan Steinkruger', 'password': '6547', 'email address': ''},
    {'name': 'Robert Rushing', 'password': '7634', 'email address': ''},
    {'name': 'Eric Miller', 'password': '8563', 'email address': ''},
    {'name': 'Chi Kuba', 'password': '7653', 'email address': ''},
    {'name': 'Tyler Shackelford', 'password': '765357', 'email address': ''},
    {'name': 'Mathew Sichette', 'password': '8352', 'email address': ''},
    {'name': 'Justin Wilkes', 'password': '2345', 'email address': ''},
    {'name': 'Jason Roy Alvarez', 'password': '5324', 'email address': ''},
    {'name': 'Christopher Trower', 'password': '46781', 'email address': ''},
]

# Turn the seed data into a list of Drivers objects
Drivers_objects = []
for item in seed_data:
    v = Drivers(name=item["name"], password=item["password"], email_address=item['email address'])
    Drivers_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(Drivers_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# SELECT * FROM driver info
Drivers = session.query(Drivers).all()

print('INSERTED driver info:', Drivers)
print('')  # separator

for v in Drivers:
    print(v.name, v.password, v.email_address)

print('')  # separator

# SELECT * FROM driver info ORDER BY name, color
Drivers = session.query(Drivers).order_by(
    Drivers.name, Drivers.password, Drivers.email_address).all()

for i, v in enumerate(Drivers):
    print(str(i+1) + ". " + v.formatted_name())

# ... rest of model definition

    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()




#######################################

class Cars(Base):
    __tablename__ = "Cars"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    license = Column(String, nullable=False)
    year = Column(String, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)


# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'license': 'D', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Ford', 'model': 'ARCA'},
    {'license': 'B', 'year': '1953', 'make': 'Chevrolet', 'model': 'ARCA'},
    {'license': 'C', 'year': '1953', 'make': 'Ford', 'model': 'ARCA'},
    {'license': 'B', 'year': '1953', 'make': 'Chevrolet', 'model': 'ARCA'},
    {'license': 'C', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Ford', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'B', 'year': '1953', 'make': 'Ford', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Ford', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Chevrolet', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Toyota', 'model': 'ARCA'},
    {'license': 'D', 'year': '1953', 'make': 'Chevrolet', 'model': 'ARCA'},
]

# Turn the seed data into a list of Cars objects
Cars_objects = []
for item in seed_data:
    v = Cars(license=item["license"], year=item["year"], make=item["make"], model=item["model"])
    Cars_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(Cars_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# SELECT * FROM Cars
Cars = session.query(Cars).all()

print('INSERTED Cars:', Cars)
print('')  # separator

for v in Cars:
    print(v.license, v.year, v.make, v.model)

print('')  # separator

# SELECT * FROM Cars ORDER BY name, color
Cars = session.query(Cars).order_by(
    Cars.name, Cars.year, Cars.make, Cars.model).all()

for i, v in enumerate(Cars):
    print(str(i+1) + ". " + v.formatted_name())

# ... rest of model definition

    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()