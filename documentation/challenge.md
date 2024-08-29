# Back End Notification APIs
It is required to create a notification system API, which is capable of receiving a message and depending on the category of the message and the users subscribed to them, said users will be notified to the medium that they themselves chose.
3 categories of messages will be handled:
- Sports
- Finance
- Films
And it is required to send 3 types of notifications:

- SMS
- E-mail
- Push Notification

It is not required that any message is actually sent or communicates with any external API, only the sending of said notification will be recorded in a Logs file or in the database.
In the log it is required to save all the necessary information to identify that the correct notification was made to the corresponding user. Save information such as the type of message, type of notification, user data, time, etc.
User administration is not required, a Mock of users can be managed in the system, they must have the following information:

- ID
- Name
- E-mail
- Phone
- Subscribed [ ] List of categories you are subscribed to
- Channels [ ] List of user notification types (SMS | Email | PushNotification)

The API will receive 2 parameters:
- Category. Validate from the list of available categories
- Message. Just validate that the message is not empty.

## We will evaluate:
- Best practices: Validations and handle exceptions, Intuitive names, and OOP.
- Solid Principles: Separation of concerns, Abstraction and scalability, Inferface usage, Dependency inversion.
- Design Patterns: One or more design patterns implemented to solve the main problem, select the proper channels and send notifications.
- Architecture: Well architecture design, have a well defined folder structure and separation of concerns, scalable and prepared for minimum changes on new requirements in the future. (Routes/Controllers/Services/Repositories, DTOs / Interfaces / etc.).
- Unit Testing: Tests for each service and function, Multiple test scenarios per function.
- Database: Migrations and Seeders, Foreign keys usage (In case of RDBMS), Indexing, Proper data types and length and Load all catalogs in the database (Is a plus).
- Challenge: Requirements accomplish, Performance and search methods, Fault tolerance on sending notifications and Scalable to add more notification channels.