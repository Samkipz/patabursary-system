# Pata Bursary

Pata Bursary is a bursary allocation system for universities and colleges, built using the Django web framework.

## How to Install and Run

### Prerequisites

Ensure you have the following installed:
- Python 3 (version 3.8 preferred due to `backports.zoneinfo==0.2.1`)
- PostgreSQL

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Samkipz/patabursary-system.git
   cd patabursary-system
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv env
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     source env/Scripts/activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

You should now be able to access the application at `http://127.0.0.1:8000/`.


# Screenshots

Applicant profile
![Screenshot (370)](https://user-images.githubusercontent.com/27472221/222946826-7808a248-c0b6-4ba3-87e2-2ad051c88e48.png)

Admin Approve applicants mobile view
![Screenshot (368)](https://user-images.githubusercontent.com/27472221/222947034-9a4fc60d-d6fa-4ffa-a787-c582d4f33c0b.png)

## Contributing

For support and contribution. Feel free to reach out.
