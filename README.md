# Digital Hub

## Overview

Digital Hub is a platform designed to facilitate collaborative problem-solving between students and mentors. The platform enables users to post and manage problem statements, match students with mentors based on their interests and expertise, and engage in real-time communication through integrated chat and video conferencing tools.

## Features

- **Problem Statement Management**: Allows users to post, browse, and manage a list of problem statements for collaborative projects.
- **Matching System**: Students are assigned to mentors based on their areas of interest and expertise, ensuring relevant and effective collaboration.
- **Real-Time Communication**: Integrated tools for chat and video conferencing support seamless collaboration between students and mentors.
- **User Profiles**: Students and mentors can create and manage profiles to showcase their skills, interests, and previous projects.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Django Templates).
- **Backend**: Django or another web framework (Python).
- **Database**: PostgreSQL or another relational database.
- **Authentication**: Secure login and user management with Django's built-in authentication system.

## Getting Started

### Prerequisites

- Python installed on your system.
- Virtualenv for creating isolated Python environments.
- PostgreSQL installed and running.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akhilsai0099/DigitalHub.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DigitalHub
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   - Update the database settings in `settings.py` to match your PostgreSQL (or other) configuration.
   - Apply migrations to set up the database schema:
     ```bash
     python manage.py migrate
     ```
6. Create a superuser for accessing the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Open your browser and navigate to `http://localhost:8000` to access the platform.

### Usage

- **User Registration/Login**: Create a new account or log in with existing credentials.
- **Post Problem Statements**: Users can create and manage problem statements for collaborative projects.
- **Matching**: The platform automatically matches students with mentors based on their profiles and project requirements.
- **Real-Time Collaboration**: Use the integrated chat and video conferencing tools to discuss and work on projects.
