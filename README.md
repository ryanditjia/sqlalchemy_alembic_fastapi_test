Need help with:

> ModuleNotFoundError: No module named 'fairphonic_data'

Steps to replicate:

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Rename .env.example to .env
5. Make Postgres db named fairphonic_new
6. `cd fairphonic_data`
7. `alembic revision --autogenerate -m "Initial Migration"`

Possible fixes:

https://alembic.sqlalchemy.org/en/latest/front.html#installation

It says to run development environment in editable mode (pip install -e .). But I’m not familiar with this.
