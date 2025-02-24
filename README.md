# 🐾 PetCare Connect

**PetCare Connect** is a web application designed to help pet owners find trusted caregivers for their pets when they need to travel or step away.

## 🌟 Features

### 🏡 For Pet Owners
- **Find Caregivers** – Browse profiles of verified pet sitters in your area.  
- **Pet Profiles** – Add detailed information about your pets, including age, breed, medical needs, and personality.  
- **Booking System** – Use a calendar-based scheduling system with reminders for easy booking.  
- **Ratings & Reviews** – Read and leave reviews to ensure the best care for your furry friend.  
- **Private Chats** – Connect with caregivers instantly through secure messaging.  
- **Community Forum** – Engage with other pet lovers, ask questions, and explore trending topics.  

### 🐶 For Caregivers
- **Become a Caregiver** – Apply to become a trusted pet sitter by filling out a simple form.  
- **Caregiver Verification** – Upload certifications or references to build trust with pet owners.  
- **Availability Management** – Set your availability with an integrated calendar.  

### 📅 Additional Features
- **Rate & Review** – Share your experience by rating and reviewing caregivers after each service.  
- **Personal Calendar** – Keep track of all pet care requests and bookings in one place.  

---

## 🛠️ Technologies Used
- **Backend:** Django 4.2  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, JavaScript  
- **Styling:** Custom CSS  
- 

## 🚀 Getting Started

To run the project locally on your machine, follow these steps:

1. **Clone the Repository**:
    Download the project code to your local machine using Git.


2. **Create and Activate a Virtual Environment**:
    Set up a virtual environment to isolate project dependencies:
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Dependencies**:
    Install the required dependencies listed in the requirements.txt file:
    ```bash
    pip install -r requirements.txt

    ```

4. **Configure the Environment Variables**:
    Create a .env file in the root directory, and if you have the necessary credentials and configurations ready, add them securely to the file.


5. **Set Up the Database**:
    Apply database migrations to create the necessary tables:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

    ```

6. **Create a Superuser**:
    To access the Django Admin panel, create a superuser account:
    ```bash
    python manage.py createsuperuser
    ```
   

7. **Run the Development Server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```
  After starting the server, open your web browser and go to:
  http://127.0.0.1:8000/  
