# An OOP project of an Airport Terminal
This was an OOP project undertaken to deliver specfic user stories (Scrum artifact) of an airport terminal, predominantly from the perspective of an airport assistant. User stories set out below.

## Terminal user stories

- As a user, I want to add new passengers to a flight list.
- As a user, I wan to create a passengers name and passport number so i can add them to a flight.
- As a user, I want to create a flight trip with a specific destination.
- As a user, I want to be able to assign and/or change a plane to my flight trip, input my password so I can handle the problem. 
- As a user, I would like to generate a flight attendees list that lists the passengers name and passports so that I can check attendee documents.

## The structure
The approach was to start with three different classes, the people class, the plane class and the flight class. Then from the people class there would be two subclasses that inherit from the people class; the staff class and the passenger class. Following a seperations of concerns all the classes are its own module and the run file is where all the classes, methods and attributes are used to create instances for the terminal. The runfile is a program that asks the airport assistant for inputs and responds with the according outputs. The runfile always starts with a password entry.

## The runfile result
The runfile (after correct pasword entry), welcomes users to the current flight in progress display and the offers the following services: Flight status, Flight manifest, Assign staff, Add passenger
and Exit. 

### Flight status
Shows the flight details that include the flight name, departure, destination, flight time, plane, capacity, pilot and co pilot. It will allow the user to change the flight by either delaying the flight time, diverting the flight to a different destination or changing the plane used for the flight.

### Flight manifest
Allows the user to see three different flight attendee lists, passenger, crew and full. All the list will names, dob's, nationality, boarding pass, passport number, ticket type for passengers and airline, title and tax number for staff.
  
### Assign staff
Allows the user to assign existing staff from the staff roster to the flight.

### Add Passenger
 Allows the user to create new passengers. First the user needs to confirm they want to add the passenger to the flight by name. Passengers are created by entering the passenger name, dob, nationality, passport number, ticket type. This is looped so the user needs to select "n" when asked to add passenger to flight. When passengers are added they can be viewed in the flight manifest.
 
 ### Project criticisms
 I think the testing can be more robust by using testing libraries. Also, with more iterations the terminal could be more sophisticated eg. have a web frontend. However this project was very useful in understanding how to use OOP in python and create working code. 