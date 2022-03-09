# Generated by Django 2.2.2 on 2020-08-04 13:05
from django.db import migrations, models
import django.db.models.deletion
import models_logging.models
from models_logging.settings import LOGGING_USER_MODEL, USE_POSTGRES, DJANGO_MAYOR_VERSION

operations = [
    migrations.AlterField(
        model_name='change',
        name='user',
        field=models.ForeignKey(blank=True, help_text='The user who created this changes.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=LOGGING_USER_MODEL, verbose_name='User'),
    ),
    migrations.AlterField(
        model_name='revision',
        name='comment',
        field=models.TextField(blank=True, help_text='A text comment on this revision.', verbose_name='comment'),
    ),
    migrations.RemoveField(
        model_name='change',
        name='comment',
    ),
]

if USE_POSTGRES and DJANGO_MAYOR_VERSION >= 4:
    from django.db.models import JSONField
elif USE_POSTGRES:
    from django.contrib.postgres.fields import JSONField

    operations.append(
        migrations.AlterField(
            model_name='change',
            name='changed_data',
            field=JSONField(
                blank=True,
                encoder=models_logging.models.get_encoder,
                null=True
            ),
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('models_logging', '0004_auto_20171124_1445'),
    ]

    operations = operations
