from django.apps import AppConfig


default_app_config = '{{ cookiecutter.repo_name }}.SiteConfig'

LEONARDO_APPS = ['{{ cookiecutter.repo_name }}']


class SiteConfig(AppConfig):
    name = '{{ cookiecutter.repo_name }}'
    verbose_name = "{{ cookiecutter.project_name }}"
