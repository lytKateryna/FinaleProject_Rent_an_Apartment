# Rent an Apartment API

Final Backend Project — REST API platform for apartment rental.

---

# Technologies

- Python
- Django
- Django REST Framework
- MySQL
- Docker
- Docker Compose
- JWT Authentication
- Swagger / OpenAPI
- AWS EC2 deployment

---

# Description

This project is a backend system for apartment rental.

The project supports different user roles:

- Anonymous user
- Tenant
- Landlord
- Admin / Superuser

---

# User Roles

## Tenant

Tenant users can:

- Browse apartment listings
- Search and filter properties
- Create bookings
- Leave reviews after completed bookings
- View their own bookings

## Landlord

Landlord users can:

- Create apartment listings
- Update their own listings
- Delete their own listings
- View bookings related to their properties
- Manage their rental properties

## Admin

Administrators can:

- Manage all users
- Access all bookings
- Delete bookings
- Access protected endpoints
- Fully manage the platform

---

# Main Features

## Authentication

- User registration
- User login
- JWT authentication
- Logout
- Role-based access

## Listings

- Create listings
- View listings
- Update own listings
- Delete own listings
- Filter by:
  - city
  - district
  - price
  - rooms
  - property type
- Search by:
  - title
  - description
  - city
  - district
  - street
- Ordering by:
  - price
  - creation date

## Bookings

- Create booking
- View own bookings
- Landlords can view bookings for their listings
- Booking status management
- Booking overlap validation
- Users cannot book their own listings
- Only admins can delete bookings

## Reviews

- Users can leave reviews only after completed bookings
- Reviews are displayed inside listing details
- Reviews are publicly available

## Search History

- Search queries are saved
- Popular search keywords endpoint
- Protected search history endpoints

## Listing Views

- Listing views tracking
- Popular listings support
- Protected listing views endpoints

---

# Permissions

## Anonymous users can

- View listings
- Search listings
- Filter listings
- View reviews
- View popular search keywords

## Authenticated users can

- Create bookings
- Leave reviews after completed bookings

## Landlords can

- Create listings
- Update their own listings
- Delete their own listings
- View bookings related to their properties

## Admins can

- Manage users
- Delete bookings
- Access protected system endpoints

---

# API Documentation

Swagger documentation:

```text
/api/schema/swagger/
```

---

# Installation

## Clone repository

```bash
git clone https://github.com/lytKateryna/FinaleProject_Rent_an_Apartment.git
cd FinaleProject_Rent_an_Apartment
```

## Create `.env`

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=rent_app
DB_USER=rent_user
DB_PASSWORD=your_password
DB_HOST=database
DB_PORT=3306

DOCKERHUB_USER=your_dockerhub_username
APP_NAME=django-diploma-app
APP_TAG=latest
```

---

# Run with Docker

## Build and start containers

```bash
docker compose up -d --build
```

## Apply migrations

```bash
docker compose exec web python manage.py migrate
```

## Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

# Local Development

```bash
docker compose -f docker-compose.local.yaml up -d --build
```

---

# Deployment

The project is containerized with Docker and deployed on AWS EC2.

Example deployment commands:

```bash
docker compose pull web
docker compose up -d
docker compose ps
```

# Project Structure
```text
rent_ads/
│
├── __init__.py
├── migrations/
│
├── models/
│   ├── __init__.py
│   ├── address.py
│   ├── booking.py
│   ├── listing.py
│   ├── listing_view.py
│   ├── review.py
│   ├── search_history.py
│   └── users.py
│
├── serializers/
│   ├── __init__.py
│   ├── address.py
│   ├── auth.py
│   ├── booking.py
│   ├── listing.py
│   ├── listing_view.py
│   ├── review.py
│   ├── search_history.py
│   └── users.py
│
├── urls/
│   ├── __init__.py
│   └── auth.py
│
├── views/
│   ├── __init__.py
│   ├── auth.py
│   ├── bookings.py
│   ├── listing_views.py
│   ├── listings.py
│   ├── reviews.py
│   ├── search_histories.py
│   └── users.py
│
├── permissions.py
├── middlewares.py
├── utils.py
├── admin.py
├── apps.py
└── tests.py

renthub/
│
├── __init__.py
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py
'''
.dockerignore
.env
Dockerfile
docker-compose.yaml
docker-compose.local.yaml
requirements.txt
manage.py
README.md
```

---

# Author

Kateryna Lytvynenko

GitHub:
https://github.com/lytKateryna