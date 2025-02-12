Secure Code Review SystemOverviewThe Secure Code Review System is a web-based application that helps manage user authentication, motion detection, and real-time notifications using Flask, SQLite, and WebSockets.
Features✅ User Authentication: Secure login/logout with JWT-based authentication.✅ Real-time Notifications: Uses Flask-SocketIO for live updates.✅ Motion Detection: Updates user availability based on motion and Bluetooth device status.✅ Search & Filtering: Allows searching for users in the database.✅ Role-based Dashboard: Displays user details dynamically based on authentication.✅ Security Features: Uses hashed passwords and token-based authentication.
Technologies Used🛠 Backend: Flask (Python)🗄 Database: SQLite🔐 Authentication: JWT (JSON Web Tokens)🎨 Frontend: HTML, CSS, JavaScript⚡ Real-time Communication: Flask-SocketIO, WebSockets🔒 Security: Hashing (SHA-256), JWT token protection
Installation📥 Clone the Repositorygit clone https://github.com/yourusername/secure-code-review.git
cd secure-code-review📦 Install Dependenciespip install -r requirements.txt🚀 Run the Applicationpython app.pyor using Flask-SocketIO:
python -m flask run --host=0.0.0.0 --port=80Usage🔑 Login: Users can log in with their email and password.
📊 Dashboard: Displays the status of logged-in users.
🔔 Real-time Updates: Notifications are pushed via WebSockets.
🔍 User Search: Find users based on username.
🚪 Logout: Clears the authentication token.
API Endpoints📌 / - Home Page📌 /login - User Login📌 /logout - User Logout📌 /dashboard - User Dashboard (Requires Authentication)📌 /search - Search for users📌 /status - Update user status📌 /timings - Update availability timings📌 /your_endpoint - Receive motion and Bluetooth data
Contribution1️⃣ Fork the repository.2️⃣ Create a new branch (feature-branch-name).3️⃣ Commit your changes.4️⃣ Push to your fork and create a Pull Request.
