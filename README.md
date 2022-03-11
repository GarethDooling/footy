# Fantasy Footy - QA DevOps Boot Camp Final Project 

# Brief

- To create a web application that integrates with a database and demonstrates CRUD functionality.
- To utilise containers to host and deploy the application.
- To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy the application.

The final deliverables for the project are:

1. A GitHub repository containing all of the code written for this project, including the software source code, Jenkins configuration, Docker configuration and any related scripts.
2. The GitHub repository should also contain the write-up for the project in the form of a README.md file.
3. Also required is video evidence of the application and CI/CD pipeline working.

## Part 1: Project Design

According to the MoSCoW principles, I proposed to create a simple fantasy football application relating to two tables; 'Teams' and 'Players'. The app MUST demonstrate CRUD functionality so a user is be able to create, read, update and delete teams and players. 

Unfortunately, I was not able to add the second 'Players' table so the app only demonstrates CRUD for the 'Teams' table. 

As a result, I was not able to add any further SHOULD/COULD/WOULD elements to the project. 

## Part 2: Architecture

### 2.1 Entity Diagrams

The initial plan was for a one to many relationship between the databases however, unfortunately, I was not able to link the two databases together. 

![image](https://user-images.githubusercontent.com/97617047/153581704-25a4ffb8-81b2-491a-acf4-ed42351c7833.png)

### 2.2 CI/CD Pipeline

The diagram below shows how the CI/CD pipeline should operate.   

![129537075-43c17f22-2709-4441-b00c-710398d07310](https://user-images.githubusercontent.com/97617047/157854508-bd8f2f02-71b6-4946-baf4-a213691df359.png)

The Jenkins pipeline had four stages; set up, test, create schema and run however I was not able to enable the test stage.

![image](https://user-images.githubusercontent.com/97617047/157857460-59cbb23b-d9d2-4112-a8c4-4396d60a22c3.png)

Although by omitting the test stage I was able to cause the other three stages to run successfully.

![image](https://user-images.githubusercontent.com/97617047/157857906-51cfd6ce-fbbc-406b-b3ac-c635b6c10809.png)

## Part 3: Project Tracking

Jira was used to keep track of the project and the link is: https://garethdooling.atlassian.net/jira/software/projects/FF2/boards/2

![image](https://user-images.githubusercontent.com/97617047/157858494-cb83cf1c-a8d0-4832-b609-50e397ab1b2e.png)

## Part 4: Risk Assessment

Some of the risks which need to be considered and mitigated. 

![image](https://user-images.githubusercontent.com/97617047/157861073-d22203cc-c094-4828-b494-d2e7ce147e34.png)

## Part 5: Testing

Unit tests were written to test the app using pytest and achieved 80% coverage on the entire code. 

![image](https://user-images.githubusercontent.com/97617047/157863282-1258a670-f61d-4290-bb17-b84994f0a89c.png)

On the app.py file only one out of the four tests were successful. 

![image](https://user-images.githubusercontent.com/97617047/157864198-0cb6f52a-2d75-4969-9b12-395da92eeff1.png)

## Part 6: Front End Design

The app has a very simple layout with user input text boxes and buttons for CRUD functionality. 

![image](https://user-images.githubusercontent.com/97617047/157864698-18056bb6-0369-48cb-9151-64dc6915d06b.png)

![image](https://user-images.githubusercontent.com/97617047/157864777-c4120efd-8430-4ed3-99c0-3a960be94523.png)

![image](https://user-images.githubusercontent.com/97617047/157864957-7ddfe787-b0a1-48a8-88ae-9c10436573d0.png)

![image](https://user-images.githubusercontent.com/97617047/157865021-c608e4a8-8f9e-48e8-b3c3-7bf97065c8c1.png)

## Part 7: Issues & Improvements

Obviously I was not able to fulfil the brief however at least I was able to demonstrate basic CRUD functionality and make use of the Jenkins pipeline. 

In future, I would like to be able to fix the testing issues and then proceed to complete the brief inn full. 

## Part 8: Deliverables

Link to the Vimeo video - https://vimeo.com/687046440/b1a9fca6ae

## Part 9: Author & Acknowledgements

Author - Gareth Dooling
Acknowledgements - htr-volker, The Earl of Grey & Cleon909 for design & layout of readme documents
