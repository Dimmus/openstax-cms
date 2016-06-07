OpenStax CMS
=======================

Built using [Wagtail CMS](http://wagtail.io).

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [Python](https://www.python.org/) >= 3.4
* [PIP](https://github.com/pypa/pip) >=8.0.0

### Installation

With PostgreSQL running (and configured to allow you to connect as the 'postgres' user - if not, you'll need to adjust the `createdb` line and the database settings in openstax/settings/base.py accordingly), run the following commands:

    git clone https://github.com/Connexions/openstax-cms.git
    cd openstax-cms
    pip install -r requirements/dev.txt
    createdb -U postgres openstax
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

### Testing

Run with ``./manage.py test --liveserver=localhost:8001 --settings=openstax.settings.dev``

### SQLite support

SQLite is supported as an alternative to PostgreSQL - update the `DATABASES` setting
in openstax/settings/base.py to use `'django.db.backends.sqlite3'` and set `NAME` to be the full path of your database file, as you would with a regular Django project.
