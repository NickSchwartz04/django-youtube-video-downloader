This project is a Django based web app that allows users to download videos off of Youtube.com. 

Features

Simply enter a link from any youtube video
Sends the video file back to the user for download

Requirements

Python > 3.x
Django
Pytubefix

Usage guide

Clone the repo: 
git clone https://github.com/NickSchwartz04/django-youtube-video-downloader.git
cd django-youtube-video-downloader
Then active the virtual environment:
python3 -m venv venv
source venv/bin/activate
Finally run migrations:
python manage.py makemigrations
python manage.py migrate
An start the server:
python manage.py runserver

Credits: Based on tutorial by GeeksforGeeks https://www.geeksforgeeks.org/python/python-web-development-django/ with modifications/additions by Nicholas Schwartz
