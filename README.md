# Django Blog Web Application

## Overview
This repository contains a Django-based blog web application that allows users to create, edit, and manage blog posts, as well as interact with content through comments. The app features user authentication, category filtering, and a clean, responsive design using Bootstrap.

## Features
- **User Authentication**: Sign up, log in, and log out functionality.
- **Post Management**: Create, edit, delete, and view blog posts.
- **Comment System**: Users can comment on posts and view comments.
- **Category and Date Filtering**: Easily navigate posts by categories or publication dates.
- **Responsive Design**: Mobile-friendly interface using Bootstrap.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/django-blog-web-app.git
Navigate to the project directory:
cd django-blog-web-app
Create and activate a virtual environment:


python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies:

pip install -r requirements.txt
Apply migrations:

python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Access the application:
Open your browser and go to http://127.0.0.1:8000/

Usage
Admin Panel: Manage users, posts, categories, and comments from the Django admin interface (/admin).
User Registration and Login: Users can register and log in to create and comment on posts.
Post Creation: Authenticated users can create, edit, and delete their own posts.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request for review.

License
This project is licensed under the MIT License. See the LICENSE file for details.
