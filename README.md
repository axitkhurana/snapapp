# SnapApp

Django app for snaps


## What?

Create albums from Facebook automatically.


## How?

The updatealbum custom django command fetches between 1 to 5 pictures. Add it to cron to run every 10 minutes
After 60 mins or 12 pictures the album is full and an email is sent.


## Where?

Access albums:
* in your browser at: http://127.0.0.1:8000/snapapp/
* send api requests to get them


## Anything else?

Yeah, the directory structure:
+
|- foreversnap/         ▸ the django app
|- django-foreversnap/  ▸ the packaged app for pypi
|- screenshots/         ▸ screenshots of the app
|- README.md            ▸ readme file
'- requirements.txt     ▸ requirements file for virtualenv

Checkout README.txt in django-foreversnap to read more on how to set up the app.


## Snaps Please!

Albums page:
![Albums page](https://raw.github.com/axitkhurana/snapapp/master/screenshots/1.png)

------

Snaps page:
![Snaps page 1](https://raw.github.com/axitkhurana/snapapp/master/screenshots/2.png)

![Snaps page 2](https://raw.github.com/axitkhurana/snapapp/master/screenshots/3.png)


## Why?

Just playing around with
* django custom manage.py commands
* packaging
* facebook api
