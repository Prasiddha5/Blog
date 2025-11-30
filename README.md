Blog API – Backend Internship Assignment (Intuji)

This project is a clean and professional implementation of a "Blog API" built using **Django REST Framework**.  
It is submitted as part of the **Backend Developer Internship Assessment** for **Intuji**.

The API supports:
- Creating a blog
- Listing all blogs
- Retrieving a blog by ID
- Updating a blog
- Each blog has exactly one category

A Postman Collection is included to allow quick testing of all endpoints.

Features

✔ Create a blog  
✔ Get all blogs  
✔ Get a blog by ID  
✔ Update a blog  
✔ Category validation using TextChoices  
✔ Clean & scalable Django REST architecture  
✔ Automatic timestamps  
✔ Professional code structure  
✔ Postman Collection included  

---

Project Structure

Blog/
├── blog_api/ # Main Django project
├── blogs/ # App containing models, views, serializers
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── postman_collection.json # API requests for testing
├── manage.py
└── requirements.txt


---

Installation & Setup

1. Clone the repository:
"it clone https://github.com/Prasiddha5/Blog.git
cd Blog"

2. Create a virtual environment
python -m venv env
source env/bin/activate        # macOS/Linux
env\Scripts\activate           # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the server
python manage.py runserver

#You will be live at:
http://127.0.0.1:8000/api/blogs/

Postman Collection:
A ready to use Postman Collection is included: Blog_api.Postman_collection.json

Technology Used:
-Python
-Django
-Django REST Framework
-SQLite 
-Postman

Author:
-Prasiddha Baidhya
Github: https://github.com/Prasiddha5
