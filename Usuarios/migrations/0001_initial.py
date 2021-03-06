# Generated by Django 2.1.3 on 2018-11-13 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('produce_contenido', models.BooleanField(default=False)),
                ('numero_recetas', models.IntegerField(default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profilepicture',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuarios'),
        ),
    ]
