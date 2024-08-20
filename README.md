# Blog-Web-apps
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
cd django-blog-web-app


python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`pip install -r requirements.txt


pip install -r requirements.txt


python manage.py migrate

python manage.py createsuperuser

python manage.py runserver



