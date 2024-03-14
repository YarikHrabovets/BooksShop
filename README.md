# Web application using Django
#### Video Demo: https://youtu.be/2kw8AS_cAIU
___
#### Description:
I decided use `django` because it was developed in a fast-paced 
newsroom environment, it was designed to make common web development tasks 
fast and easy. <br />
_**Advantages of using django:**_
- Automatically generated admin panel.
- Full-featured.
- Security.
- Scalability.

Also, I used `Bootstrap 5` to perform highly responsive and fancy design. <br />
_**Advantages of using bootstrap:**_
- mobile-first approach
- Using Bootstrap for web design provides a responsive grid system 
that automatically adjusts the responsive layout based on the screen size, 
ensuring your website looks great on various devices.
- Being open-source and free, Bootstrap provides a cost-effective solution for web designers.
- Bootstrap's extensive customization options also allow you to personalize the appearance and style of your website.
- Bootstrap is easy to implement, making it accessible.

This project was made with certain goal - make reading process easier on the internet. 
Also site provides a platform for people to discover and save books.<br />
_**Site allows people use several advantages of it:**_
- read books
- add books to the personal list
- remove books from the personal list
- store personal list and manage it
- edit profile page

In addition, you can easily filter books by author or genres. Furthermore, you are able to check author's biography or genre definition.

_**Project structure:**_
```
   BooksShop
   |
   |__finalproject
   |
   |__requirements.txt
```
`finalproject` contains django structure that contains all project files and dirs. <br />
You may find interesting:
- `books` is the app folder in which:
  - `migrations` contains migrations that can be applied to the database;
  - `static` contains all static files(css, images, js);
  - `templates` contains all html files. And you can use `django jinja` with them;
  - `admin.py` module used to define the administration interface for your application's models. Django provides a powerful and customizable admin interface that allows you to perform various administrative tasks such as creating, updating, and deleting records in your database without having to write custom views and templates. The admin.py file plays a crucial role in configuring this admin interface;
  - `apps.py` module used to configure and manage the Django application or app itself. It's a part of the app's metadata and is typically located inside the app's directory;
  - `froms.py` module used to define and manage forms for your web application. Forms are a fundamental part of web development as they allow users to input data, which can then be processed and validated on the server. Django provides a powerful and flexible way to define forms using Python classes;
  - `managers.py` module used to define custom managers for your models. A manager in Django is a class that encapsulates a set of database queries for a particular model. By defining custom managers in the managers.py file, you can encapsulate complex or frequently used database queries, making your code more organized and maintainable;
  - `models.py` is a central component of the Django ORM (Object-Relational Mapping) system. It is used to define the data models for your web application. Models define the structure and behavior of the database tables used by your application, and they are used to interact with the database in a high-level, Pythonic way;
  - `tests.py` module for your own unit tests and test cases for your Django application. Testing is a crucial part of software development, and Django provides a testing framework that allows you to write and run tests to ensure that your application's functionality works correctly and to catch potential bugs or regressions;
  - `urls.py`  module used to define URL patterns for your web application. URL patterns specify how URLs are mapped to views within your Django project. This file is a crucial part of defining the routing and URL structure for your application;
  - `views.py` module used to define the view functions or classes that handle incoming HTTP requests and return HTTP responses. Views are a fundamental component of a Django web application, and they are responsible for processing user requests, interacting with models and data, and rendering templates or returning JSON responses;
- Another `finalproject` dir in which:
  - `settings.py` settings for project;
  - `asgi.py / wsgi.py` play important roles in serving your web application using different server interfaces;
  - `urls.py`  module used to define URL patterns for your web application. URL patterns specify how URLs are mapped to views within your Django project. This file is a crucial part of defining the routing and URL structure for your application;

To run local: <br />
Make sure you are in `BooksShop` folder and then:
```sh
    $ pip install -r requirements.txt
    $ cd finalproject
    $ python manage.py runserver
```
>Superuser login detail(email: super@test.com, password: foo)

___
### Thank you for attention!
