
USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

SITE_ID = 1
SITE_NAME = '{{ cookiecutter.project_name }}'

# redirect migrations
MIGRATION_MODULES = {
    'web': '{{ cookiecutter.repo_name }}.migrations.web',
    'elephantblog': '{{ cookiecutter.repo_name }}.migrations.blog',
    'media': '{{ cookiecutter.repo_name }}.migrations.media',
    'leonardo_module_links': '{{ cookiecutter.repo_name }}.migrations.links',
    'team': '{{ cookiecutter.repo_name }}.migrations.team',
    'form_designer': '{{ cookiecutter.repo_name }}.migrations.forms',
}
