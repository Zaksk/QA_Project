# QA_Project

### contents 
* [Introduction](#introduction)
    * [Objective](#Objective)
    * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [CI Pipeline](#ci-pipeline)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)


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


### CI Pipeline
The next requirement I will be tackling in this documentation is the implementation of different stages of a typical CI pipeline, such as version control, development environment and build server. Continuous Integration (CI) allows developers to generate and implement new functionality with ease and speed through automation of the integration process. Building and testing of new code is handled through automation, allowing developers to focus their efforts on the creation of new features.

A continuous integration pipeline should:
* Maintain a single source code repository for a project
* Have a "master" branch that should always be ready to deploy
* Automate build processes
* Automate testing of new builds
* Inform developers of test failures with detailed logs
* Encourage smaller, frequent deployments of code

For my project tracking I decided to use Jira as it was taught to me in the first couple of weeks during my training. I begun by intialising some stories regarding the users' expecations on what they should be able to do and why, as well as my expectations from a developer's point of view. I then proceeded to define some requirements that needed to be fulfilled to classify a task as done, to give mne a more detailed idea on what needed to be done. As I moved through my tasks, the status would be updated and stories would be moved to their appropriate sections.

An example of my sprint 2 can be found down below:
![Jira](https://github.com/Zaksk/QA_Project/blob/main/jiraboard.png)  

For Version Vontrol I chose git as it allows changes to the project to be made and committed whilst keeping the commit history for access to earlier versions. For my project repository decided to host it on github as it allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing.

The development environment used was a python3 virtual environment (venv) as it allows pip installs to be made and the app to be run without affecting any conflicting pip installs on the same machine. This was hosted on a virtual machine running Ubuntu 20.04. Python is used as Flask in a Python based micro-framework. 

Jenkins was used as a build server, providing automation of building and testing. This automation is achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit.

![Pipeline](https://github.com/Zaksk/QA_Project/blob/main/pipeline.png)


## Risk Assessment
A risk assessment register was made to identify risks and recommend measures to control them. Shown below was the original planned risk assessment aswell as the
new risk assessment created after implementation. 
The likelihood and impact level 1(low Probability/Impact) to 5(High Probability/Impact) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.
![Risk Assessment](https://github.com/Zaksk/QA_Project/blob/main/risk_ass.png)


### Front-end Design 
Upon navigating to the app the user is presented with the login page:

![login](https://github.com/Zaksk/QA_Project/blob/main/login.png)

The nav bar provides links which allow the user to create an account if they do not have one otherwise. If an attempt to view the home is made, an error message will be displayed. User credentials are verified and if criteria are not met, again, warning messages will be shown. Once an account is created and the user has logged in the home page with all the products will be shown:
![sign-up](https://github.com/Zaksk/QA_Project/blob/main/sign_up.png)
![home](https://github.com/Zaksk/QA_Project/blob/main/home.png)

In this home page the user can create a product by pressing on the assigned button which will redirect them to another page and prompt them to fill up a product details.
Once a product is created the user can decide to delete or update their post.
You can also view users' post history by navigating as shown below:

![history](https://github.com/Zaksk/QA_Project/blob/main/new_top.png)


### Future improvements 

In future sprints, in addition to fixing some of the issues identified with the current version, I would like to add an option to allow users to amend their account details, as well as, purchase and leave reviews under products bought. I would also be looking to allow users to delete their accounts in case they decide to do so. 