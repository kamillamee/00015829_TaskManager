Task Manager Application
Distributed Systems and Cloud Computing

Student ID: 00015829
Repository: https://github.com/kamillamee/00015829_TaskManager.git

1. Introduction

This project presents the design and implementation of a web-based Task Manager application developed using the Django framework. The system enables users to create and manage projects, assign tasks, categorize them using tags, and monitor progress efficiently.

The application demonstrates core principles of distributed systems and cloud computing, including containerization, service orchestration, CI/CD automation, and production-ready deployment using modern DevOps practices.

2. System Overview

The Task Manager is a multi-user web application that supports project-based task management. Each authenticated user can create multiple projects, and each project can contain multiple tasks. Tasks may be labeled with tags for categorization and filtering.

The system follows a client–server architecture and is designed to operate both in a local development environment and in a cloud-based production environment.

3. Functional Requirements

The application implements the following key features:

3.1 User Authentication

User registration

Secure login and logout functionality

Role-based access via Django authentication system

3.2 Project Management

Create new projects

View a list of user-specific projects

Update project details

Delete projects

3.3 Task Management

Create tasks within a project

Assign multiple tags to tasks

Edit and delete tasks

View task details

3.4 Database Relationships

The system uses relational database modeling with the following structure:

User → Project (One-to-Many)

Project → Task (One-to-Many)

Task → Tag (Many-to-Many)

3.5 Administrative Interface

The Django Admin Panel is fully configured to allow administrative management of users, projects, tasks, and tags.

3.6 User Interface Pages

The application contains more than five functional pages, including:

Home Page

Login Page

Registration Page

Project List Page

Project Detail Page

Task Create/Update/Delete Pages

4. Technologies Used

The system is implemented using the following technologies:

Component	Technology
Backend Framework	Django 4.2
Programming Language	Python 3.11
Database	PostgreSQL 15
Web Server	Gunicorn
Reverse Proxy	Nginx
Containerization	Docker, Docker Compose
CI/CD	GitHub Actions
5. System Architecture

The application follows a containerized microservice-oriented architecture. Key services include:

Web Application Container (Django + Gunicorn)

Database Container (PostgreSQL)

Reverse Proxy Container (Nginx)

Docker Compose is used to orchestrate multi-container deployment, ensuring consistent environments across development and production.

6. Local Development Setup
6.1 Development Without Docker

The application can be executed locally using a Python virtual environment:

Create a virtual environment

Install dependencies

Configure environment variables

Apply database migrations

Run the development server

SQLite can optionally be used for lightweight local testing.

6.2 Development With Docker

For environment consistency, Docker Compose is used to build and run all services:
Environment variables are configured via .env
Containers are built and started using docker compose up --build
Application is accessible via http://localhost

7. Testing

Automated testing is implemented using pytest. Tests validate application logic, model relationships, and core functionality.
Tests can be executed using:

pytest tasks/ -v
8. Deployment Strategy
8.1 Cloud Deployment

The application is designed for deployment on cloud-based virtual machines (e.g., Ubuntu 22.04 on Azure). The deployment process includes:
Virtual machine configuration
Docker installation
Repository cloning
Environment configuration
HTTPS setup using Let's Encrypt

Firewall configuration (ports 22, 80, 443)

8.2 CI/CD Pipeline

A GitHub Actions pipeline automates:
Docker image building
Image publishing to Docker Hub
Optional automatic deployment via SSH
The pipeline is triggered upon push to the main branch, ensuring continuous integration and delivery.

9. Environment Configuration

The system uses environment variables to ensure security and flexibility. Key variables include:

SECRET_KEY – Django secret key

DEBUG – Debug mode configuration

ALLOWED_HOSTS – Production host configuration

POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD – Database credentials

DOCKERHUB_USERNAME – Docker image tagging

USE_SQLITE – Optional local database override