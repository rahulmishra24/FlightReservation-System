# FlightReservation-System

Flight Reservation system will provide the endpoints to create  and retrieve the flights details, with authenticated passenger details. It will also provide endpoints to find flights with any source and destination, and passenger can save their reservation or can cancel it .

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install django,djangorestframework,psycopg2
```

## RUN
```bash
python3 manage.py runserver
```
## Endpoints

## Flights
- Create a new flight>
    >`POST` <http://localhost:8000/flights>
- Edit the flight detail with that specific id
    > `PUT` <http://localhost:8000/flights/{id}>
- Get a list of flights along with ids
    > `GET` <http://localhost:8000/flights/{id}>
- Get list of all flights
    > `GET` <http://localhost:8000/flights>
- Delete a flight with specific id
   > `DELETE` <http://localhost:8000/flights/{id}>

## Passenger
### Register
- Register a user
    >`POST` <http://localhost:8000/api/auth/register>

### Login
- Login a user
    >`POST` <http://localhost:8000/api/auth/login>

### Logout
- Logout a user
    >`GET` <http://localhost:8000/api/auth/logout>

### Change Password
- Change user password with new password
    >`POST` <http://localhost:8000/password_change> 

## OTHER
### Find Flights
- Find flights by giving source and destination with date to travel
    >`POST` <http://localhost:8000/feature/find_flights/>

### Save Reservation
- Save Reservation with that flight id with the authenticated passenger detail.
    >`POST` <http://localhost:8000/feature/save_reservation/>





