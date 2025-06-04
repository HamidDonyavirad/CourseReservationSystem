# 🎓 Course Reservation System (Django)

This is a Django-based web application for managing and reserving educational courses. Users can sign up, browse available courses, view course details, and reserve spots. Admins can manage course listings and track enrollments.

---

## 📌 Features

- User registration and login
- Course listing with details
- Course reservation system
- Capacity validation (no overbooking)
- Admin panel for course management
- Basic styling with Bootstrap 5

---

## 🧰 Technologies Used

- Python 3.x
- Django 4.x
- SQLite (default, easily switchable to PostgreSQL, etc.)
- Bootstrap 5
- HTML, CSS

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/HamidDonyavirad/CourseReservationSystem.git
cd CourseReservationSystem
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` does not exist, install Django manually:
```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Now visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Project Structure

```
CourseReservationSystem/
├── courses/           # App for course management and reservations
├── users/             # App for user authentication (optional)
├── templates/         # HTML templates
├── static/            # CSS/JS files
├── media/             # Uploaded course images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🖼 Screenshots

<!-- Add screenshots here -->
<!-- Example:
![Course List](screenshots/course_list.png)
![Reservation Form](screenshots/reserve_form.png)
-->

---

## 🧪 Testing (optional)

You can write and run tests using Django’s built-in test framework:

```bash
python manage.py test
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to fork this project, open issues, or submit pull requests for improvements.

---

## ✉️ Contact

If you have any questions or suggestions, feel free to contact [Hamid Donyavirad](https://github.com/HamidDonyavirad).
