# Django Medical Research Management System

## Description:
This project is a Django-based web application designed to help doctors and medical professionals create, manage, and track research projects. The system allows users to log in, create research projects, view research data, and manage user profiles. It integrates a robust backend with a user-friendly frontend, enabling seamless management of medical research data.

## Key Features:
1. **User Authentication**: Users can register, log in, and manage their profiles securely.
2. **Research Management**: Doctors can create, update, and delete research projects.
3. **Project Details**: Each research project can have a title, description, and a creator (doctor) associated with it.
4. **Analytics Dashboard**: Provides a visual representation of research data, including statistics and trends.
5. **CRUD Operations**: Full CRUD functionality for managing research projects.
6. **Admin Functionality**: Admins can manage users and research projects, ensuring proper data management and access control.
7. **User Management**: Admins can create, update, and delete users with different roles (Doctor, Admin).
8. **Database Integration**: PostgreSQL database for storing user information and research project data.
9. **Responsive UI**: Simple, user-friendly web interface with navigation to manage research data and view analytics.

## Features Implemented:
- **Login and Registration**: Doctors can securely log in and register as users of the system.
- **Create and Manage Research Projects**: Doctors can create and manage their research projects, with fields for title and body of the research.
- **Research Listings**: Users can view all research projects they are associated with, and the system lists all available projects.
- **Admin Dashboard**: Admins can access a dashboard to manage users, research projects, and view analytics data.
- **Analytics Dashboard**: Displays important statistics, such as the number of ongoing and completed research projects.
- **User Management**: Admins can manage user accounts, update roles, and delete users if necessary.
- **Database Integration**: PostgreSQL database to manage user data and research project information.
- **Responsive UI**: Simple, user-friendly interface with navigation options to manage research data and user accounts.

## Requirements:
To run this project, you need to have the following installed:
- **Python 3.8+**
- **Django 3.2+**
- **PostgreSQL Database**
- **Required Python Libraries**: Listed in the `requirements.txt` file

## Installation:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ChristianRukundo/django-medical-research.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-medical-research
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
    - Create a database in PostgreSQL.
    - Update your database connection settings in the `settings.py` file.

5. Run migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

8. Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.

## URL Routing and Views:

### User Authentication Routes:
- **Login**: `/users/login/` - User login page.
- **Logout**: `/users/logout/` - User logout page.
- **Registration**: `/users/register/` - User registration page.

### Research Management Routes:
- **Create Research**: `/researches/create/` - Form to create a new research project.
- **List Research**: `/researches/` - List of all research projects.
- **Research Detail**: `/researches/{id}/` - View details of a specific research project.
- **Update Research**: `/researches/{id}/update/` - Edit a specific research project.
- **Delete Research**: `/researches/{id}/delete/` - Delete a specific research project.

### Admin Dashboard Routes:
- **Admin Dashboard**: `/admin/` - Access to the Django admin dashboard where admins can manage users, research projects, and other data.

### Analytics Dashboard:
- **Research Analytics**: `/analytics/` - View the analytics dashboard showing research project statistics, such as total projects, completed projects, and active research.

## Technologies Used:
- **Backend**: Django, Python, PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL

## Contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

