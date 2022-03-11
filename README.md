# QA_Project

### contents 
* [Introduction](#introduction)
    * [Objective](#Objective)
    * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Footer](#footer)

### Objective
In this project I will be attempting to complete all the requirements set by our trainer to display what I have learnt during the last couple of weeks. 

The main goal was to develop a fully functional python coded application capable to interact with the user through the implementation of CRUD(Create, Read, Update and Delete) Functionality.

On top of this, I was also required to provide the following:
* A clear documentation - Outlining the design, architecture and risk assessment
* A relational database, which consists of at least two tables with a one-to-many relation
* A Trello board
* A front-end website using Flask
* The code needed to be integrated via a Version Control System, built using a CI server and deployed to a cloud-based virtual machine
* Test suites 

### My Approach
To achieve this, I have decided to produce a simple product trading shop that must allow the user to do the following:
* Create a user account (satisfies 'Create') that stores:
   * *User Name*
   * *First and Last Name*
   * *Email*
   * *Password*
* Create posts of products that they would like to sell (satisfies 'Create') with the following information:
   * *Title* of the product
   * *Author* of the product
   * *Date and time* that the product was posted
   * *Price* of the product
   * *Category* that the product belongs to
   * *Description* of the product 
* View and update their posts (satisfies 'Read' and 'Update')
* Delete their posts (satisfies 'Delete')
* View products that other users have created (satisfies 'Read')

Additionally, I would like to allow the user to:
* Add products to their basket and then process the order
* Message sellers privately regarding a specific item they are selling
* Add reviews on items after they purchased them
* View and edit their accounts 


## Architecture
### Entity Relationship Diagram
I decided to create two tables, one for users and one for products with a one-to-many relationship which is potrayed by the image below:  

![erdiagram1](https://github.com/Zaksk/QA_Project/blob/main/erd.png)

My initial thoughts however, were diffrent, in fact I had planned to create a many to many relationship, on top of the one I have created, between the product table and an order table using an order_line table as the child entity. My initial ERD was as follow:

![erdiagram2](https://github.com/Zaksk/QA_Project/blob/main/erd2.png)