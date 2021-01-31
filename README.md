# Django Improvement
## How get started

### Set Up

```shell
git clone https://github.com/Cohey0727/qiita_django_improvement.git
cd qiita_django_improvement
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata dump.json
touch logs/query.log
```

### Run Examples

```shell script
python manage.py shell
>>> from query.models import *
...
```

### Tail SQL

```shell script
tail -f logs/query.log
```

### Update Dump
```shell script
python manage.py daumpdata --exclude auth --exclude contenttypes > dump.json
```
