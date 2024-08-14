## Prerequisites

- Python 3.12
- Django 5.1
- PostgreSQL 
- Docker

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Caxaro4ekPixel/SFW_TEST.git
cd app
```

### 2. Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up the database:

```bash
POSTGRES_DB=name # Replace with your database name
POSTGRES_USER=user # Replace with your database username
POSTGRES_PASSWORD=password # Replace with your database password
POSTGRES_HOST=db # Replace with your database host (e.g., db)
POSTGRES_PORT=5432 # Replace with your database port (e.g., 5432)
SECRET_KEY=random_string # Replace with a random secret key
DEBUG=False # Set to True for development, False for production
```

### 5. Apply migrations:

```bash
python manage.py migrate
```

### 6. Generate initial test data:

```bash
python manage.py seed
```

### 7. Test the application:

```bash
python manage.py test_contract --id 32812
```

## Using Docker (Optional)

### 1. Build and start the Docker containers:

```bash
docker compose up -d
```

### 2. Test the application:

He will execute this command himself, but why not check once again?)

```bash
docker-compose exec web python manage.py test_contract --id 32812
```

## Project Structure

+ **core/models.py**: Contains the Django models for the application.
+ **core/management/commands/test_contract.py**: Contains the custom management command.
+ **core/management/commands/seed.py**: Contains the command for seeding the database with initial data.
+ **docker-compose.yml**: Docker Compose configuration for setting up the application with PostgreSQL.
+ **Dockerfile**: Docker configuration for the Django application.
