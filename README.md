This is web app for commenting some posts in real time with django channels.

Installation instructions:

1. Clone the project - git clone (ssh link, or https)
2. Go to directory /chat/
3. Install virtual environment (python3 -m venv myenv)
4. Activate virtual environment: Windows (myenv\Scripts\activate), unix (source myenv/bin/activate)
5. Install relations - pip install -r requirements.txt
6. Go to directory chat/posts and run python manage.py migrate
7. Run redis server (redis-server)