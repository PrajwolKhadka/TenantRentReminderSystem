# TenantRentReminderSystem 🏠🗓️

The Tenant Rent Reminder System is a robust and automated application designed to streamline the rent collection process for landlords and property managers. It helps in efficiently managing tenant records and ensuring timely rent payments by sending automated reminders before the due date.

🌟 Features
This system provides a centralized platform for property management tasks, focusing on minimizing administrative burden and improving cash flow.

Tenant Management: A CRUD interface to easily add, view, update, and delete tenant records, including contact information and rent specifics.

Automated Reminders: Schedule and send automated rent payment reminders to tenants via Whatsapp.

Payment Tracking: Mark rent payments as Paid or Unpaid to maintain an accurate payment history for each tenant.

Dashboard Overview: A simple, intuitive dashboard showing upcoming rent due dates, overdue payments, and overall occupancy status.

Customizable Due Dates: Set specific monthly due dates for each tenant.

Secure Authentication: User authentication for landlords/managers to ensure data privacy and security.

🛠️ Technology Stack
The project is built using the popular Python web framework, ensuring scalability and maintainability.

Backend: Python

Web Framework: Django (Inferred based on manage.py)

Database: PostgreSQL/MySQL (for production)

Whatsapp Services: Twilio (trial account)

🚀 Getting Started
Follow these steps to set up the project locally.

Prerequisites
You need the following software installed on your system:

Python 3.8+

pip (Python package installer)

Git

Installation: 

git clone https://github.com/PrajwolKhadka/TenantRentReminderSystem.git

cd TenantRentReminderSystem



git clone https://github.com/PrajwolKhadka/TenantRentReminderSystem.git

cd TenantRentReminderSystem

Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies:



python -m venv venv

source venv/bin/activate  # On macOS/Linux

# venv\Scripts\activate  # On Windows

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Create a file named .env in the root directory and add your secret keys and database/email configuration.

Code snippet


# Twilio Configuration in .env file
TWILIO_ACCOUNT_SID=A****************8

TWILIO_AUTH_TOKEN=e3aaaaaaaaaaaaaaaaaaa

TWILIO_SANDBOX_NUMBER=whatsapp:+(countrycode)(number)

PHONE_NUMBER=your phone number for esewa/khalti

Run Migrations

Apply the initial database schema:



python manage.py migrate

Create a Superuser

Create an administrator account to access the Django admin and the property management dashboard:



python manage.py createsuperuser

Run the Server

Start the Django development server:



python manage.py runserver

The application will now be running at http://127.0.0.1:8000/admin/.

📝 Usage

Adding Tenants

Navigate to the Admin Panel (/admin) and log in with the superuser account.

You can use the built-in Django Admin to add your initial tenants, or access the custom tenant creation page (e.g., /tenants/add).

Enter the tenant's details, rent amount, and the rent due day of the month.

The system will automatically check the due dates and dispatch reminders based on your configured schedule (e.g., 3 days before the due date).

🤝 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'feat: Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📞 Contact
Prajwol Khadka - prazolkhadka67@gmail.com

Project Link: https://github.com/PrajwolKhadka/TenantRentReminderSystem