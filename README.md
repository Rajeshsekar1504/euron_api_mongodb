🚀 FastAPI + MongoDB CRUD API

A simple asynchronous REST API built using FastAPI and MongoDB Atlas, featuring:

✔ Create

✔ Read (all + single)

✔ Full update (PUT)

✔ Partial update (PATCH)

✔ Delete

This project also includes phone number validation using Pydantic, and secure environment variables using .env & .gitignore.

| Technology        | Purpose                |
| ----------------- | ---------------------- |
| **FastAPI**       | API Framework (Python) |
| **Motor**         | Async MongoDB Driver   |
| **MongoDB Atlas** | Cloud Database         |
| **Pydantic**      | Data Validation        |
| **Uvicorn**       | ASGI Server            |
| **dotenv**        | Read `.env` file       |

mongodb-api/
├── main.py
├── requirements.txt
├── .env                 # (Not committed to GitHub)
├── .gitignore
└── README.md            # ← you are reading this

1️⃣ Clone this repository
git clone https://github.com/Rajeshsekar1504/euron_api_mongodb.git
cd euron_api_mongodb

2️⃣ Create a virtual environment
python -m venv myenv
myenv/Scripts/activate         # Windows
source myenv/bin/activate      # Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add .env file (not uploaded to GitHub)
Create a .env file with:
MONGO_URL="your_mongodb_atlas_connection_string"

📌 Run the Application
uvicorn main:app --reload

Visit Swagger UI (API documentation) at:
👉 http://127.0.0.1:8000/docs

🧾 API Endpoints

| Method     | Endpoint      | Description     |
| ---------- | ------------- | --------------- |
| **POST**   | `/euron`      | Insert data     |
| **GET**    | `/euron`      | Get all data    |
| **GET**    | `/euron/{id}` | Get single data |
| **PUT**    | `/euron/{id}` | Full update     |
| **PATCH**  | `/euron/{id}` | Partial update  |
| **DELETE** | `/euron/{id}` | Delete record   |


🔐 Important

⚠ Do NOT push .env or myenv/ to GitHub
Use this .gitignore:

# Virtual environment
myenv/

# Environment variables
.env

# Cache files
__pycache__/
*.pyc

🚀 Deployment Suggestions
| Platform   | Status                   | Supports          |
| ---------- | ------------------------ | ----------------- |
| Render     | 🟢 Free                  | FastAPI + MongoDB |
| Railway    | 🟢 Free                  | FastAPI + MongoDB |
| Fly.io     | 🟡 Free limited          | FastAPI           |
| Deta Space | 🟠 MongoDB not supported | FastAPI only      |

🧭 Future Enhancements

🔐 JWT Authentication (Login / Signup)

📄 Pagination & Filtering

📦 Docker Support

🔁 Async Queue with Celery / Redis

🧪 Unit Testing (pytest)

🧑‍💻 Author

Your Name
💼 LinkedIn: https://www.linkedin.com/in/rajesh-sekar-data-analyst/
🐙 GitHub: https://github.com/Rajeshsekar1504
📧 Email: sekarsrajesh7@gmail.com








