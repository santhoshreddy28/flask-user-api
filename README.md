# 🚀 Full Stack User Management System

## 📌 Description

This is a full stack web application built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend. The application allows users to perform basic CRUD operations such as adding, viewing, and deleting users through an interactive dashboard.

The project demonstrates how frontend and backend systems communicate using REST APIs and real-time data updates.

---

## 🌐 Live Demo

👉 https://flask-user-api-1.onrender.com/

---

## 🚀 Features

* Add new users
* View all users
* Delete users
* Interactive frontend dashboard
* Real-time API integration
* JSON response handling
* Clean and simple UI

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **API:** RESTful API
* **Deployment:** Render

---

## 📂 Project Structure

```
flask-user-api/
│
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/santhoshreddy28/flask-user-api.git
cd flask-user-api
```

2. Install dependencies:

```
python -m pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### GET /users

* Fetch all users

### POST /users

* Add a new user
* Request Body:

```
{
  "name": "Santhosh",
  "email": "user@example.com"
}
```

### DELETE /users/<index>

* Delete user by index

---

## 💡 Learning Outcomes

* Built a full stack application from scratch
* Implemented REST APIs using Flask
* Integrated frontend with backend
* Practiced CRUD operations
* Deployed a live application on cloud

---

## 🔮 Future Improvements

* Add database (SQLite/PostgreSQL)
* Implement authentication system
* Improve UI with React
* Add update/edit functionality

---

## 👨‍💻 Author

**Gajjala Lakshmi Santhosh Reddy**
GitHub: https://github.com/santhoshreddy28

---
