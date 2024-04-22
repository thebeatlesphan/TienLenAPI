# TienLen API

This project will be a test drive with FastAPI

# IMPORTANT PYTHON PACKAGES

pip install fastapi\
pip install uvicorn\ (migrated to hypercorn for server workers)
pip install install "hypercorn[trio]"


## INSTRUCTIONS 

clone repo\
cd pathToRepo\
```gunicorn main:app --workers 4 --worker-class```\
(this will host program at your localhost / 127.0.0.1)\

```hypercorn --worker-class trio --workers 4 --reload main:app```
--bind localhost:port

# BACKEND

No db will be required here\
from pydantic import BaseModel (validation for data types)\

## Deployment Concepts

* Security / HTTPS
	- TLS Termination Proxy: provides encryption for API
		e.g Traefik, Caddy, Nginx, HAProxy, Kubernetes w Ingress Controller, cloud provider
	- HTTPS certificates
* Running on startup
	- Constantly available
* Restarts
* Replication (the number of processes running)
* Memory
* Previous steps before starting

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

Definition - Stateful Protocols require the server to save the state of a process\
Response Mechanism - Stateful expects a response and if no answer is received, the request is resent\
Design Complexity - This makes the design heavy and complex since data needs to be stored\
Requirement of Server - The server is required to store and save status information and details of sessions\
Dependency - Server and Client are tightly coupled, as in extremely interdependent on each other\
Transaction Handling - Transaction handling is relatively slow in the stateful protocol\
Implementation - They are logically eavy to implement\
Functioning After a Crash - Since stateful protocols need to store data regarding the sessions, once the crash occurs, all the stored data is lost. Hence, it doesn't work very well after a crash occurs\
Design - The server design is complex to implement\
Working State - They react only by the current state of a transaction or request\
Requests - Requests are always dependent on the server side\
Userbase - These are a thing of the past, and the dynamic user base is very less\
Servers Specifications - The same server must be utilized to process every request\
Scaling Architecture - Scaling architecture is difficult and complex\
Programming - It is difficult to code as one of the salient features here is data storage\
Examples - Telent, FTP (File Transfer Protocol), etc

#### Stateless

Definition - Stateless Protocols do not need the server to save the state of a process\
Response mechanism - In stateless, the client sends a request to a server, which the server responds based on the state of the request\
Design complexity - Server design is simplified in this case\
Requirement of server - No server is needed for data storage\
Dependency - Server and Client are more independent and hence, loosely coupled\
Transaction handling - This is relatively faster in the stateless protocol\
Implementation - They are easy to implement\
Functioning after a crash - In the event of a crash, stateless protocols work better because there doesn't exist a state that needs to be restored. A server that failed during the crash can simply be restarted\
Design - The server design is dimpler to implement\
Working State - They act independently by taking the previous or next request into consideration\
Requests - Requests are self-contained and not dependent on the server side\
Userbase - These are the future because more and more industries are moving towards statelessness\
Servers Specifications - Different servers can be used to process different information at a time\
Scaling Architecture - It is relatively easier to scale architecture\
Programming - It is much easier to code\
Examples - HTTP, UDP (User Diagram Protocol), DNS (Domain Name System), etc

# FRONTEND

The frontend will be responsible for rendering and handling the complete session state.

# Software Engineering Principles

1) manage using a phased life-cycle plan
2) perform continuous validation
3) maintain disciplined product control
4) use modern programming practices
5) maintain clear accountability for results
6) use better and fewer people
7) maintain a commitment to improve the process

* KISS (Keep It Simple, Stupid)
* DRY (Don't Repeat Yourself)
	- Inheritance and Composition
	both allow you to write code in one place and then reuse it at other places
	- Database Normalization
	is a design technique used in databases to eliminate redundance (repetition) of data
* YAGNI (You Aren't Gonna Need It)

S - SRP (Single Responsibility Principle)\
	Every function, class, module, or service should have a single clearly defined responsibility\
O - OCP (Open Closed Principle)\
	Open for extension but closed for modification\
L - LSP (Liskov Substitution Principle)\
	Every child/derived class shoulbe be substitutable for their parent/base class without altering the correctnes of the program\
I - ISP (Interface Segregation Principle)\
	Client should never be forced to depend on methods it does not use\
D - DIP (Dependency Inversion Principle)\
	Avoid tight coupling between software modules

## JavaScript File Structure Best Practices

1. Comment Your Code
2. Use ES6 Classes
3. Use Promises in Your JavaScript Data Structures
4. Keep Things Separated
5. Use Constants and Enums

* async functions should implement try / catches

### Event Propagation

1. Capture phase - Starting from window, document and the root element, the event dives down through ancestors of the target element
2. Target phase - The event gets triggered on the element on which the user has clicked
3. Bubble phase - Finally, the event bubbles up through ancestors of the target element until the root element, document, and window

### Event Delegation

Instead of attaching the event listeners directly to the buttons, you delete listening to the parent. When a button is clicked, the listener of the parent element catches the bubbling event.

1. Determine the parent of elements to watch for events
2. Attach the event listener to the parent element
3. Use event.target to select the target element