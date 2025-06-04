from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CronJobLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, db_index=True)),
                ('start_time', models.DateTimeField(db_index=True)),
                ('end_time', models.DateTimeField(db_index=True)),
                ('is_success', models.BooleanField(default=False)),
                ('message', models.TextField(max_length=1000, blank=True)),
                ('ran_at_time', models.TimeField(null=True, blank=True, db_index=True, editable=False)),
            ],
        ),
    ]
