# 🐾  PetCare Connect

## 🌟 What Exactly is the Project About?  

**PetCare Connect** is a web application designed to help pet owners find trusted caregivers for their pets when they need to travel or step away.

In more detail **PetCare Connect** is a community-driven platform where:  

- **Pet owners** can connect with trusted caregivers to ensure their pets receive the best care.  
- **Users** can ask questions, share experiences, and gain valuable insights about pet care.  
- The platform fosters **collaboration and trust** through forums, direct interactions, and verified caregiver profiles.  


## 🌟 Features
- **Find Caregivers**: Browse profiles of potential pet sitters in your area.  
- **Become a Caregiver**: Even if you don't have a pet, and you just want to take care of one, just fill the Caregiver form and become one.
- **Ratings and Reviews**: Check ratings and reviews from other pet owners to ensure your furry friend is in safe hands.  
- **Rate and Review**: Share your experience by rating and reviewing caregivers after the service.  
- **Connect with Confidence**: Build a reliable network of pet lovers who are ready to help.
- **Private Chats**: Connect with pet-lovers and caregivers with just one click.
- **Forum**: Ask all the questions you have in the PetCare forum or just scroll to see the most liked categories and posts.
- **Calendar**: Keep track of your schedule, once you request a care or the opposite put it easily in your personal calendar.

## 🏡 For Pet Owners
- **Pet Profiles**: Add detailed profiles for pets, including age, breed, medical needs, and personality.
- **Booking System**: Calendar-based system to schedule pet care with reminders.

## 🐶 For Caregivers
- **Caregiver Verification**: Allow uploading certifications or references for trust.
- **Availability Management**: Set availability through a calendar.

## 🔑 Application Usage

### 🌍 Public Part  
- **Home Page** – A welcoming introduction to the platform, where users can learn about the platform's features.  
- **About Us** – Provides an overview of **PetCare Connect**, its creators and their mission, and how it helps pet owners and caregivers.  
- **Pets Profiles Page** – Users can view details about registered pets.
- **Pet Details Page** - Users can view more detailed information about specific pet, including breed, age, owner and more.
- **Caregivers Page** – Users can browse all available caregivers, view their profiles, and check their ratings.  
- **Contact Page** – Provides ways to reach out for support or inquiries related to the platform.  
- **FAQ Page** – Displays frequently asked questions, organized into categories, to help users understand how the platform works. Guests can only view content, while registered users have full interaction privileges.  
- **Login Page** – Allows existing users (both pet owners and caregivers) to log in securely using their credentials.  
- **Register Page** – Enables new users to create an account by providing basic information. Users can register as either pet owners or caregivers.  
- **Forum Page** – A discussion space where users can engage with other pet lovers, ask questions, and share pet care experiences.  
- **Threads and Posts Pages** – Displays discussion threads where users can participate in pet-related conversations.  
- **My Calendar Page** – Allows caregivers to manage their availability and pet owners to track scheduled pet care sessions.  

### 🔒 Private Part  
- **My Profile Page** – Users can view and manage their personal information, including their pet if they have one.  
- **My Requests Page** – Pet owners and caregivers can view and manage their pet care requests, including pending and confirmed bookings.  
- **Chat System** – Enables private messaging between pet owners and caregivers for better coordination.  
- **Become a Caregiver Form** – Allows users to apply as caregivers by providing necessary details such as experience, availability, and certifications.  
- **Caregivers Page** – Authenticated users can rate specific caregivers and leave a review.
- **Add Profile of Pet Form** – Lets pet owners add detailed profiles of their pets, including medical history and special requirements.  
- **Create and Like Posts in Forum Page** – Registered users can start new discussion threads, reply to posts, and like helpful content.  
- **Logout Page** – Allows users to log out of the application securely.  

## Next steps:
-Add feature to create new categories and threads for authenticated users.

## 🛠️ **Technologies Used**
- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS


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
