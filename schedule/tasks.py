from django.core.management import call_command

from project_root.celery import app


@app.task()
def create_cells_for_two_weeks_task():
    call_command("create_cells_for_two_weeks")


@app.task()
def set_for_all_users_restricton_on_use_task():
    call_command("set_for_all_users_restricton_on_use")
