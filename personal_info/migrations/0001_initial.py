from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('course', models.CharField(max_length=100)),
                ('year_level', models.PositiveSmallIntegerField()),
                ('section', models.CharField(blank=True, max_length=50)),
                ('enrollment_status', models.CharField(choices=[('enrolled', 'Enrolled'), ('graduated', 'Graduated'), ('on_leave', 'On leave'), ('withdrawn', 'Withdrawn')], default='enrolled', max_length=20)),
                ('academic_year', models.CharField(blank=True, max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('home_address', models.TextField(blank=True)),
                ('guardian_name', models.CharField(blank=True, max_length=150)),
                ('guardian_relationship', models.CharField(blank=True, max_length=50)),
                ('emergency_contact', models.CharField(blank=True, max_length=30)),
                ('blood_type', models.CharField(blank=True, max_length=5)),
                ('allergies', models.TextField(blank=True)),
                ('medical_conditions', models.TextField(blank=True)),
                ('physician_contact', models.CharField(blank=True, max_length=100)),
                ('background_info', models.TextField(blank=True)),
                ('extracurriculars', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'student_id'],
            },
        ),
    ]
