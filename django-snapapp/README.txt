=======
SnapApp
=======

SnapApp is a simple Django app that helps to create albums automatically'

Quick start
-----------

1. Add "snapapp" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'snapapp',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^snapapp/', include('snapapp.urls')),

3. Run `python manage.py syncdb` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
  to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/snapapp/ to view your album.

To create an album:
1. Add your facebook api token to management/commands/updatealbum.py file
2. Create crontab entry for running the update album command every 10 minutes 
