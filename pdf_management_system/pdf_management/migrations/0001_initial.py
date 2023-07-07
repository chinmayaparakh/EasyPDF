# Generated by Django 4.2.3 on 2023-07-07 15:36

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
            name='UploadedFiles',
            fields=[
                ('unique_url', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=256)),
                ('file_path', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SharedFiels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField()),
                ('shared_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_management.uploadedfiles')),
                ('shared_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_management.uploadedfiles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
