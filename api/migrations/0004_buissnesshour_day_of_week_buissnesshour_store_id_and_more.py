# Generated by Django 4.2.1 on 2023-06-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_timezone_timezone_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='buissnesshour',
            name='day_of_week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buissnesshour',
            name='store_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='report_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('running', 'Running'), ('completed', 'Completed')], default='running', max_length=20),
        ),
        migrations.AddField(
            model_name='storestatus',
            name='store_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timezone',
            name='store_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
