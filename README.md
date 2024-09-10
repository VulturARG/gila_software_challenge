# Gila Software Challenge
## General considerations
According to the [technical requirements](docs/challenge.md) I designed a system based on the following assumptions:
- The system must be able to process large amounts of data. Iterables are used instead of lists, generated using the yield command.
- The requested system is part of a system that will continue to grow in the future, incorporating new functionalities.
- The system must be able to scale in the future.
- A change may be required in some of the technologies currently used.

For these reasons I chose a design based on [hexagonal architecture](docs/hexagonal_architecture.md).
This architecture is one of the most used within Clean Architectures.
It uses the concepts of Clean Code, SOLID Principles and design patterns, such as the repository pattern among others.
It consists of isolating all the business logic itself from all external agents such as frameworks, databases, ORMs, etc.
This feature allows to generate code that is scalable, reusable and easily testable.

I consider that for this challenge FastAPI is the tool that allows to solve the requirements in the fastest and most efficient way possible.

## Design considerations
As general development rules I have the following criteria:
- **API Implementation**: I use three layers (directories) to specify the chosen architecture, using the Vertical Slice pattern within them:
- **Infrastructure**: Layer where all the external elements of the system are, such as the DRF, the implementation of the adapters and the implementation of the dependency injections. (Wirings Directory). It is the external layer of the system.
- **Application**: Layer where the use cases of the system are managed. It is the intermediate layer of the system.
- **Domain**: Layer where the business logic of the system is managed. In it are the services, which are those that implement the business logic, the positions or repositories (Abstract Classes) and the entities that manage the data. It is the internal layer of the system.
- **Files**: Every independent class or function must be in its own file. The only place where this rule is not followed is with exception families.
- **Own error handling**. Definition of a base exception, from which all other exceptions inherit. In turn, several types of basic exceptions are defined, from which exception families are generated according to a particular type of error. This design allows defining a decorator that handles errors in the different implemented methods, avoiding code repetition. In the particular case of FastAPi, a proprietary decorator is used to channel system exceptions, using the proprietary response message standard.
- **Test coverage**. The code must have the highest test coverage possible. Multiple unit tests and an integration test were done.

In this particular case, secure access to the endpoint was not implemented, since it was not a requested requirement.

The code was standardized running the [Isort](https://pypi.org/project/pytest-isort/), [Black](https://pypi.org/project/black/) and [Flake8](https://pypi.org/project/flake8/) applications.

## Installation, execution and automatic testing
- [Using virtual environment](docs/virtual_env_install.md)

## Using the system
Using the link http://127.0.0.1:8000/docs/ you can access the interactive documentation of the application (Swagger) and test the endpoint.

### Usage procedure
- A POST request is sent to the endpoint http://127.0.0.1:8000/notification with the following body:
```bash
{
"category": "string", # category must be sports, finance or films
"message": "string" # message can't be empty
}
```

If the body does not have the correct parameters, the corresponding error message will be received.
Given the purpose of the system, in a real case, message notification would be done through the asynchronous execution of an external API.
For example, you could use the Producer/Consumer pattern by using RabitMQ or Kafka messages.
This is why I chose to have the response to a request have status 202.