# Generated by Django 2.0.1 on 2018-02-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_month', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paid_on', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Student')),
            ],
        ),
    ]
