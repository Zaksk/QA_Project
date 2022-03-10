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