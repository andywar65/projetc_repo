# project_repo
A starter project for Django 3.0
## Features
Features a custom User and Profile management, user messages, a Blog and a
Nested Pages app. Uses Filebrowser and Django Private Storage for handling
images and files and Streamblocks to compose pages.
## Install
Clone the repository, use requirements.txt to install dependencies. Copy secrets_move_out_of_repo.json out of repository, rename to secrets.json and fill
in the global settings. Duplicate project/settings/base_sample.py and
project/urls_sample.py renaming to base.py and urls.py, add other installed apps
and urlpatterns. In project/static do the same for base.css, favicon.ico and
logo.png for custom styles. Migrate, collectstatic and createsuperuser.
## Deployment
In production use manpro.py instead of manage.py and point server to
wsgi_prod.py instead of wsgi.py.
