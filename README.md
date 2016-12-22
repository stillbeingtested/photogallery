### Installation instructions:

1) checkout the project

2) install system lib dependencies from system_libs.txt. Use instructions for your operation system

3) install python dependencies from requirements.txt

```
pip install -r requirements.txt
```

3.5) configure database in settings.py

4) apply migrations

```
python manage.py migrate
```

5) use django shell to load test data
```
python manage.py shell
> from photo.utils import *
> populate_database()
```

6) start application and enjoy!
```
python manage.py runserver
```