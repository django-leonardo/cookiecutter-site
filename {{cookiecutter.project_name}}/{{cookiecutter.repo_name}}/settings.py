

# Application definition

APPS = []

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1
SITE_NAME = '{{ cookiecutter.project_name }}'

# redirect migrations
MIGRATION_MODULES = {
    'web': '{{ cookiecutter.repo_name }}.migrations.web',
    'elephantblog': '{{ cookiecutter.repo_name }}.migrations.blog',
    'media': '{{ cookiecutter.repo_name }}.migrations.media',
}
