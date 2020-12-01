# GraphCenter

[Link to website](https://https://graphcenter.herokuapp.com/)
## Mission:

The mission of GraphCenter is to make their services as accessible as possible, both great projects and small assingments alike. This website allows them to show customers what
typical services they can easily provide aswell as maintaining a clear line of communication. What we would like to bring is a clear picture of the cost for single assignments and
make it easy to purchase them. With back and forth communication we would like to help you make your business endeavours a success! 


![Our Site](wireframes/Mockup.png)


### Target Audience:
* Age : 20-50 year olds
* Self-Employed Entrepeneurs
* Project leaders in bigger firms
* Marketing directors
* Self-employed Web-developers
* Private Citizens with an interest in Graphical design for their personal projects

## Welcoming the User
GraphCenter aims to keep it's User Experience engaging. With strong colours on eachother like Yellow, Purple and Black, we hope to keep the senses hooked.
Here is how we keep it simple:

#### As a customer, I would like to easily navigate all the services possible.

#### As a customer, I would like to easily contact the people at GraphCenter.

#### As a customer, I would like to see every service in detail

#### As a customer I would like to add services and store them, so I can leave the website and come back with my memory stored

#### As a customer, I would like to have a a good overview of what I want to buy and how much it would cost.

#### As a customer, I would find it important that my order is confirmed by email.

#### As a customer, I would like to give my billing information before I start looking for services to purchase.

#### As a customer, I would like to save my billing information after a purchase for when I return.

#### As a customer, I would like to view my order history and see all the orders I have made.

#### As a Graphcenter Employee, I would like to easily find the orders that customers made.

#### As a Graphcenter Employee, I would like to direct contact that customers made with us, aswell as the information to reply.

#### As a Graphcenter Employee, I would like to have safeguards if we have an error in our form.

#### As a Graphcenter Employee, I would like to be able to add/update/delete orders in an easy manner.

#### As a Graphcenter Employee, I would like to be able to add/update/delete services in an easy manner.

#### As a Graphcenter Employee, I would like to be able to find images users sent.

#### As a Graphcenter Employee, I would like to be able to find images users sent.


## Features

* __Register/login:__ User is able to login or register the moment they enter the website
* __Contact:__ Allows the User to directly contact GraphCenter.
* __Get_All_Services:__ Gets all the Services
* __Get_Service_By_Category:__ Gets the Services based on Category
* __Service_detail:__ Gets the full information of a service and allows people to add to cart.
* __Add_to_cart:__ Allows users to store information in a 'cart' to return to later
* __Create_Profile:__ Automatically done when registering, allows the user to fill it in.
* __Check_Order_History:__ Allows the user to view all the services he has made in the past.
* __Go_To_Checkout:__ Allows user to go to the checkout page and take their bag with them
* __Pay_with_CC:__ Allows the user to pay for the service, online and secure, via stripe
* __Add_file:__ Allows the user to add a file to the order
* __Add_comment:__ Allows the user to delete an already existing movie, granted they insert the right security code
* __Webhooks:__ Even if customer cancels order halfway, the order will have been put in webhooks and thus secured

### Features Left to Implement

* File on Orderline: File input on line items, 1 file per orderlineitem
* Prior work: Allows people to look at and search through work we as a company have completed
* Comments: Commenting on said private work
* Rating/like: Allowing users to rate graphic design services


### Strategy
The goal of the system is to a create easy-to-use, accesible lay-out so customers know what they can do within a few seconds on the website.
It needs to be flashy so users truly want to get to see what lays ahead.

### Scope
The goal is to make a clear cut path to what the customer might want. Contact us directly? There is a button on the main page. Want to buy services? Sign up and you're ready to go!
This way its also easier for our own employees to understand what is going on and find the way to change services or orders fast and easy.

### Structure
The system is structured to get the right information as quickly as possible. The order of the options provided are placed in a logic workflow while the design provided 
will use a messages bar that should be easy to understand and gives the customer a straight away no-nonsense feedback.
The navbar is available when needed and a footer is provided with a contact-button below the page.

### Skeleton
The Skeleton is quite obvious. The functionality is split up in applications and tend to care for their own templates, models and forms. 
There are crossovers between Profiles, Checkout and services connected by foreign keys. The services themselves are stored in the sessionId 
aswell as the authentication of the user.

### Surface
The colours chosen are yellow, red, black and purple. These colours go well together but make for a powerful look.
The buttons are styled in 2 versions; full red or yellow, to fit the overall design. 

## Technologies

* ### Languages
    * ### [Python](app.py)
    * #### HTML()
    * #### CSS()
    * #### JavaScript()
      * From Html and CSS dynamics to webhooks
    * #### [Jquery](https://jquery.com/)
      * Navigate the DOM more easily and connects Javascript functions to HTML elements
    * #### [Stripe](https://stripe.com/en-nl)
      * For credit card transactions
* ### Framework
    * #### [Django](https://www.djangoproject.com/)
      * Used for running a webapp, templating and many more functionalities
    * #### [pillow](https://pillow.readthedocs.io/en/stable/)
      * Used for interacting with the MongoDB databas
    * #### [Bootstrap](https://getbootstrap.com/)
      * Used for responsive layout and basic styles
* ### Resources
    * ### Postgress
      * Our database, holds all the records
    * ### [Heroku](https://www.Heroku.com/)
      * Hosts our website
    * #### [Google Fonts](https://fonts.google.com/)
       * Font Styles
    * ### [PEP8](http://pep8online.com/)
        * used to check and validate our python code for mistakes, inconsistencies and invalid indentation
    * #### [JSHint](https://jshint.com/)
        * Used to check Javascript code for mistakes, inconsistencies or typo's
    * #### [W3 Validator, HTML](https://validator.w3.org/#validate_by_input)
        * Used to check HTML code for mistakes, inconsistencies or typo's
    * #### [W3 Validator, CSS](https://jigsaw.w3.org/css-validator/)
        * Used to check CSS code for mistakes, inconsistencies or typo's

## Testing
    Throughout production,the HTML and CSS where checked for responsiveness and compatibillity. 
    Altough no real units testing has been done, since all forms can check themselves and will reject when non-valid information comes through

    *for admin testing on Heroku
    Username: Admin2020
    Password: Admin2021

## Bugs

### Site can't reach checkout success (still in the system!)
Initially it was thought the Imagefile on the checkout page was the issue. It didn't save correctly and takes other input than the other text fields.
Even with the help of CodeInstitute tutors, the bug couldnt be removed. It was quite the central user demand so everything was done to make it work.
After days of tinkering it was decided (due to time constaints) to remove it entirely from web application. However, it remains. 
There seems to be a mistake somewhere in the view, but i wasn't able to narrow it down in the short time that i had to complete the project.
Even now, with the deletion of the imagefield from both the models, view and form, the site doesn't go to the success_page.

#### However:

Because of the webhooks, the order still gets saved, the card still gets charged and the confirmation email sent. 
Altough the rendering to the success page isn't working, the functionality behind it does work.

### Intent before assignment (fixed!)
During the payment stage of building the web application, there were constant LocalVariable errors. After narrowing down, it turned out to be the company field.
I had intented to send the company_name with the webhooks to stripe, but stripe itself does not allow for that. Its only allowed in the meta data.
Thus it was removed from the webhook and the payment intent could be made, which means the bug was resolved and the webhooks were functional.


## Deployment

## How to the run this project locally
To run this project locally on your own IDE please follow the instructions below:

### Instructions


1.  Download a copy of the GitHub repository by clicking the "Code" button at the top right of the GitHub page and in the submenu select "Download ZIP". 
Extract the zip file to a folder of choice on your system. If Git is installed on your system, you can clone the repository with the following command:

` git clone https://github.com/Decline-of-Mind/graphcenter.git`

2. Open the unzipped folder in your preferred IDE (in this example we are using VScode) 
Open up a terminal session and set up a virtual environment with these commands in the terminal session:

If you already have virtualenv installed from a different project, then this step is not needed. The pip command may differ per system this can be pip or pip3.
`pip install virtualenv`

Your command may differ to the IDE you are using, such as python -m .venv venv ... or py manage.py ...
`virtualenv env` 

Activate the .env with the command:
`env\Scripts\activate`

This command may differ depending on your operating system, please check the Python documentation on creating an ENV.

3. Install all required django modules with the command:
`pip install -r requirements.txt`

4. Create a new file at the base directory level called env.py and copy the following into the created env.py file:

`import os`

`os.environ.setdefault( 'DEVELOPMENT', 'True')`
`os.environ.setdefault('SECRET_KEY', 'your_value')`
`os.environ.setdefault('STRIPE_PUBLIC_KEY', 'your_value')`
`os.environ.setdefault('STRIPE_SECRET_KEY', 'your_value')`

Replace <your_value> with the values from your own created accounts:

* [STRIPE_PUBLIC_KEY](https://dashboard.stripe.com/test/apikeys) Aquired from the developer's API 
* [STRIPE_SECRET_KEY](https://dashboard.stripe.com/test/apikeys) Aquired from the developer's API 
* [SECRET_KEY](https://djecrety.ir/) aquired from an online key generator

5. Set up the databases by running the following management command in your terminal:
`python manage.py migrate`

6. Create a superuser so you can have access to the django admin by running the following command in your terminal:
`python manage.py createsuperuser`

7. Finally start your server by running the following management command in the terminal:
`python manage.py runserver`

### Heroku deployment
To run this application in a cloud-based environment, you can deploy the code to Heroku. 
This section assumes you have succeeded at running the application in your local environment first, as described above.
    
1. Login to Heroku and set up a new app with an unique name (NOTE: GraphCenter is already taken)

2. On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.

3. After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku. Make sure you load the following:

| Key                   	| Value        	|
|-----------------------	|--------------	|
| AWS_ACCESS_KEY_ID     	| <your_value> 	|
| AWS_SECRET_ACCESS_KEY 	| <your_value> 	|
| DATABASE_URL          	| <your_value> 	|
| SECRET_KEY            	| <your_value> 	|
| STRIPE_PUBLIC_KEY     	| <your_value> 	|
| STRIPE_SECRET_KEY     	| <your_value> 	|
| USE_AWS               	| <your_value> 	|

Grab the DATABASE_URL link from Heroku's Config Vars as we gonna need it later to migrate to the Heroku Postgres database.

4. Now that the database on Heroku is created the following rule needs to be added to the env.py file
`os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>')`
Be certain to not share this URL with anybody.

5. Because this is a new database connection, the migrate command must be executed with the following command in your terminal:
`python manage.py migrate`

Do not forget to reactivate your virtual environment if the system or IDE is rebooted.

6. Create the superuser for the postgres database so you can have access to the django admin.
`python manage.py createsuperuser`

7. With everything set push the code to a GitHub account of yourself:
`git init`
`git commit -m 'getting ready to deploy to Heroku`
`git push -u origin`

8. From the Heroku dashboard of your newly created application, click on the "Deploy" tab, then scroll down to the "Deployment method" section and select GitHub.

9. Use the GitHub link and type in the name of the repository and click the search button. Then connect the Heroku app to the desired GitHub repository.

10. On the Deployment Tab, scroll a bit further down to the "Manual Deploy" section, select the master branch then click "Deploy Branch".

11. Once your application is running, you may want to update the Deployment method from Manual to Automatic.

12. From the Heroku dashboard select the Open app button on the top right.

## Credits
### content
The Service Illustrations came from [illlustrations.co](https://illlustrations.co/)

### Images
Home page image taken from **[Unsplash](https://unsplash.com/)
** Glen Carsten-Peters

### Acknowledgements
* __Aaron Sinnot:__ My mentor who's helped me from the conceptual phase all the way to the debugging
*__CodeInstute Tutors:__ I've had alot of help, especially with the image bug, from code institute tutors

## DISCLAIMER
Please note the content and images on this website are for educational purposes only.