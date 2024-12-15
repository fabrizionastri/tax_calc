# Django HTMX Calculator - Practical Test - Guidelines for the candidate

_Fabrizio Nastri, Nov 2024_

### Description

This repo provides the scaffolding for a simple app designed to test your knowledge of:

- Django,
- Django templating,
- HTMX.

This tech stack is seen as a possible solution for the FlexUp MVP project, in order to minimise the work in building the front end application (this may be done at a later stage). In the FlexUp MVP, we will focus on basic functionalities with minimum effort on the UX/UI side.

This test is designed to test your knowledge of the technologies mentioned above, and your ability to work with a simple front end application. The test should be completed in less than 4 hours.

### Installation

- `python -m venv .venv` : to create a virtual environment in the root folder
- `.venv\Scripts\activate` : to activate it using a build in script
- install all the dependencies with `pip install -r requirements.txt`
- make the migrations with `python manage.py makemigrations`
- run the migrations with `python manage.py migrate`
- start the server with `python manage.py runserver`

### Usage

- Open browser on http://localhost:8000/ to see the app

### App specifications / coding exercise

The root folder contains a simple stand-alone `calculator.html` page, in which the user can enter a product with the name, price and tax information. The particularity is that user can provide any 2 values of the 3 numerical values (price including tax, price excluding tax, and tax rate), and the JavaScript in the page automatically calculates the 3rd value. Use this `calculator.html` page as the starting point for the Django app template.

The goal of this exercise is to create a Django app that allows the user to store the products in a database, and to display them in a list. The user should be able to click on a product in the list to see the details of the product, and to edit the product.

### User stories / features:

- create a new product
- list all products
- view a product
- edit a product
- delete a product

### Requirements:

- The Django app has a single page, that contains:
  - the header: "Tax calculator"
  - the form
  - list of products (you need to create this table)
- The same form should be used to create, view and edit a product
- When the user submits the form:
  - the product should be saved in the database,
  - the list of products should be updated,
  - the form should be cleared.
- The list of all products should be on the same page, as table, under the form, and contain the following columns:
  - name
  - price excluding tax
  - tax rate
  - price including tax
  - a "view/edit" button
  - a "delete" button
- The user should be able to:
  - see the details of the product in the form by clicking on a "view/edit" button next to the product in the list
  - delete a product from the list and the database by clicking on a "delete" button next to the product in the list
- Column headers should be in "Title Case"
- The page should never reload, and the user should never be redirected to another page.
  - The app should use HTMX for seamless updates.
  - when a product is created, updated or deleted from the list, only that signle row should be updated in the list and the header and form should remain unchanged
  - when user clicks on a "view/edit" button, the form should be updated with the product details, and the header and list should remain unchanged
  - when user clicks on a "delete" button, the row should be removed from the list, and the header and form should remain unchanged
- Use the default Django SQLite database
