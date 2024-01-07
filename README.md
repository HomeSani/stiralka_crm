## Docs
**Recommendation: use PyCharm!!!**

### Run project
1. Clone repo:
```shell
git clone https://github.com/HomeSani/stiralka_crm.git
```
2. Set environment variables:
```shell
cp .env_example .env
```
Variables:
* Django:
   - `SECRET_KEY` - secret key for django (```wwf*2#86t64!fgh6yav$aoeuo@u2o@fy&*gg76q!&%6x_wbduad```)
   - `DEBUG` - is debug run (for deploy = ```False```)
* DataBase:
  - `DB_NAME` - database name
  - `DB_USER` - database username
  - `DB_PASS` - password for database user
  - `DB_HOST` - host for database (`0.0.0.0`)
  - `DB_PORT` - port for database (`5432`)
* RabbitMQ:
  - `RABBITMQ_USER` - username for rabbitmq
  - `RABBITMQ_PASS` - password for rabbitmq user
* Celery:
  - `CELERY_BROKER_URL` - broker url for celery, **using rabbit** (`amqp://user:mypass@rabbit:5672/`)
3. Build image:
```shell
docker-compose build
```
4. Run app:
```shell
docker-compose up
```
5. Setup pre-commits:
   1. Installation:
       ```shell
       python -m pip install pre-commit
       ```
       This command install pre-commit as global package
   2. Install (download) hooks:
       ```shell
       $ pre-commit install
       $ pre-commit run --all-files
       ```
   3. Complete. Add ```Run Git hooks``` in Git settings for Pycharm

### Setup project
1. Apply migrations:
```shell
docker-compose run app poetry run python manage.py migrate
```
2. Create superuser:
```shell
docker-compose run app poetry run python manage.py createsuperuser
```
3. Setup days (set start, end work time for day)
![](docs/setup_days.png)
4. Create settings object in model and adding days.
![](docs/create_settings.png)
5. Create cells for test (***Option**):
```shell
docker-compose run app poetry run python manage.py create_cells_for_two_weeks
```
