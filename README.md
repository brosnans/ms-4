# Milestone Project 4 - Classic Cleats eCommerce Site

*Developer: brosnans*

App available at 

 - Project Brief
 - Technologies
 - Workspace
 - Workflow
 - UXD
 - Wireframes
 - Testing
 - Heroku Deployment
 - How to Deploy Locally
 
## 1. Project Brief

In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset.
You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

**CREATE AN APPLICATION WHICH CAN BE USED FOR THE PURCHASE OF COLLECTABLE AND RARE SPORTS FOOTWEAR**

Build a web application that allows users to view and purchase collectable and rare soccer boots.

- The user is presented with a selection of the products which are for sale
- Users can browse the selection of the products which are for sale
- Users can add desired products to a shopping cart for purchase
- Users can purchase and pay for pruducts via a simple payment form

## 2. Technologies

Backend

 - Python3
 - django

Frontend

 - HTML5
 - CSS3
 - Bootstrap v3.3.7
 - jQuery v3.2.1
 - Font Awesome v4.7

Version Control

 - Git
 - Github

Database Management

 - SQLite

## 3. Workspace

**Operating System** - [Windows 10](https://en.wikipedia.org/wiki/Windows_10)

**Editor** - [Gitpod](https://gitpod.io)

**Language** - [Python3](https://www.python.org), [HTML5](https://en.wikipedia.org/wiki/HTML), [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), [Javascript](https://en.wikipedia.org/wiki/JavaScript)

**Microframework** - [django](https://www.djangoproject.com/)

**Testing**	- [Unittest](https://docs.python.org/3/library/unittest.html)

## 4. Workflow

-   Create project directory with readme
-   Create git repo
-   Work on UXD up to Skeleton plane
-   Create wireframes
-   Setup Gitpod for Python
-   Install pip3
-   Install django
-   Create requirements.txt
-   Create manage.py
-   Get django app up and running
-   Make it look nice - complete Surface plane of UXD
-   Deploy app to Heroku
-   Deploy AWS S3 for media

## 5. UXD

#### Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| _What are you aiming to achieve?_                           | View products                                                         | Allow customers to view products                |
|                                                             | Add products to shopping cart                                         | Allow customers to pay for and purchase products|
| _For whom?_                                                 | Pay for products from shopping carts using simple payment form        |                                                 |
| _TARGET AUDIENCE:_                                          | Add and remove items from shopping cart                               |                                                 |
| People who wish to purchase collectible sporting goods      |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |

#### Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Which features?                                             | Browse available products that are for sale                           | Scroll through products                         |
| What’s on the table?                                        | Add desired product to shopping cart                                  | Select product button                           |
|                                                             | Pay for products in shopping cart using simple payment form           | Shopping cart                                   |
|                                                             |                                                                       | Product payment form                            |
|                                                             |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |

#### Structure

| Focus                                                       | Interaction Design                                                           | Information Architecture                                                                |
|-------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| _How is the information structured?_                        | _Where am I? / How did I get here? / What can I do here? / Where can I go?_  | _Organizational / Navigational schemas (tree / nested list / hub and spoke / dashboard)_|
|                                                             | Browse products > View Products                                              | Tree structure                                                                          |
| _How is it logically grouped?_                              | Add Product to Shopping Cart > View Shopping Cart                            |                                                                                         |
|                                                             | Payment Form > Pay for Product                                               |                                                                                         |
|                                                             | Product Ordered                                                              |                                                                                         |
|                                                             |                                                                              |                                                                                         |

#### Skeleton

| Focus                                                         | Interface Design         | Navigational Design  | Information Design  |
|---------------------------------------------------------------|--------------------------|----------------------|---------------------|
| _How will the information be represented?_                    | See wireframes           |                      |                     |
| _How will the user navigate to the information and features?_ |                          |                      |                     |
|                                                               |                          |                      |                     |

#### Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   |                                     |
| What colours, typography and design elements will be used?  |                                     |
|                                                             |                                     |

### 6 Wireframes



### 7 Testing

[**HTML Validator Results**](https://validator.w3.org/nu/#textarea)

[**CSS Validator Results**](https://validator.w3.org/nu/#textarea)

### 8 Heroku Deployment

1. Create a new app 'ms4-ecommerce' on heroku.com

2. Install [Heroku CLI](https://devcenter.heroku.com/categories/command-line)
    - $ brew install heroku/brew/heroku

3. Login to heroku with email and password
    - $ heroku login

4. Check app is there
    - $ heroku apps

5. Add heroku remote
    - $ heroku git:remote -a ms4-ecommerce

6. Add Procfile (this tells heroku what to do with the project)
    - $ echo web: python app.py > Procfile

7. Git commit and push to heroku remote
    - $ git add Procfile
    - $ git ci -m 'Add Profile for heroku deployment'
    - $ git push -u heroku master

8. Set up dynos
    - $ heroku ps:scale web=1

9. Setup config variables on heroku dashboard

10. Restart dynos

### 9 How To Deploy Locally

```console
$ git clone git@github.com/brosnans/ms-4
$ cd ms-4
$ pip3 install -r requirements.txt
$ python3 manage.py
```

### Acknowledgements

This is for educational use.

Referenced https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce for information purposes.

Stripe integration added with help from this tutorial -

http://zabana.me/notes/how-to-integrate-stripe-with-your-django-app.html