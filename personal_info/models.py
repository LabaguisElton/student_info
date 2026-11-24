from django.db import models


class Student(models.Model):
    class EnrollmentStatus(models.TextChoices):
        ENROLLED = 'enrolled', 'Enrolled'
        GRADUATED = 'graduated', 'Graduated'
        ON_LEAVE = 'on_leave', 'On leave'
        WITHDRAWN = 'withdrawn', 'Withdrawn'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField()
    section = models.CharField(max_length=50, blank=True)
    enrollment_status = models.CharField(
        max_length=20,
        choices=EnrollmentStatus.choices,
        default=EnrollmentStatus.ENROLLED,
    )
    academic_year = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    home_address = models.TextField(blank=True)
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_relationship = models.CharField(max_length=50, blank=True)
    emergency_contact = models.CharField(max_length=30, blank=True)
    blood_type = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    physician_contact = models.CharField(max_length=100, blank=True)
    background_info = models.TextField(blank=True)
    extracurriculars = models.TextField(blank=True)

    class Meta:
        ordering = ['last_name', 'first_name', 'student_id']

    def __str__(self):
        return f'{self.last_name}, {self.first_name} ({self.student_id})'
