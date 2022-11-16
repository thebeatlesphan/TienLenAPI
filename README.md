# TienLen API

This project will be a test drive with FastAPI

# IMPORTANT PYTHON PACKAGES

pip install fastapi\
pip install uvicorn

# BACKEND

The backend will contain all the logic for the game.\
No db will be required here

## THINGS TO CONSIDER WITH API

1. Who is our target user for this API
2. Which of our products / services do we want them to be working with?
3. What are THEIR use cases for integrating with our API?
4. What technologies will they be using to integrate with our API?
5. What other services will they want our API to interact with?

### RESTful API

* No library support needed, typically used over HTTP
* Returns data without exposing methods
* Supports any content-type (XML and JSON used primarily)
* Single resource for multiple actions
* Typically uses explicit HTTP Action Verbs (CRUD)
* Documentation can be supplemented with hypermedia
* Stateless
* More difficult for developers to use

#### Stateful

Definition - Stateful Protocols require the server to save the state of a process
Response Mechanism - Stateful expects a response and if no answer is received, the request is resent
Design Complexity - This makes the design heavy and complex since data needs to be stored
Requirement of Server - The server is required to store and save status information and details of sessions
Dependency - Server and Client are tightly coupled, as in extremely interdependent on each other
Transaction Handling - Transaction handling is relatively slow in the stateful protocol
Implementation - They are logically eavy to implement
Functioning After a Crash - Since stateful protocols need to store data regarding the sessions, once the crash occurs, all the stored data is lost. Hence, it doesn't work very well after a crash occurs
Design - The server design is complex to implement
Working State - They react only by the current state of a transaction or request
Requests - Requests are always dependent on the server side
Userbase - These are a thing of the past, and the dynamic user base is very less
Servers Specifications - The same server must be utilized to process every request
Scaling Architecture - Scaling architecture is difficult and complex
Programming - It is difficult to code as one of the salient features here is data storage
Examples - Telent, FTP (File Transfer Protocol), etc

#### Stateless

Definition - Stateless Protocols do not need the server to save the state of a process
Response mechanism - In stateless, the client sends a request to a server, which the server responds based on the state of the request
Design complexity - Server design is simplified in this case
Requirement of server - No server is needed for data storage
Dependency - Server and Client are more independent and hence, loosely coupled
Transaction handling - This is relatively faster in the stateless protocol
Implementation - They are easy to implement
Functioning after a crash - In the event of a crash, stateless protocols work better because there doesn't exist a state that needs to be restored. A server that failed during the crash can simply be restarted
Design - The server design is dimpler to implement
Working State - They act independently by taking the previous or next request into consideration
Requests - Requests are self-contained and not dependent on the server side
Userbase - These are the future because more and more industries are moving towards statelessness
Servers Specifications - Different servers can be used to process different information at a time
Scaling Architecture - It is relatively easier to scale architecture
Programming - It is much easier to code
Examples - HTTP, UDP (User Diagram Protocol), DNS (Domain Name System), etc

# FRONTEND

The frontend will be responsible for rendering and handling the complete session state.

