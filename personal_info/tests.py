from django.test import TestCase

from django.urls import reverse

from .models import Student


class StudentProfileViewTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Alex',
            last_name='Santos',
            student_id='STU-001',
            course='Computer Engineering',
            year_level=2,
            section='A',
            background_info='Enjoys building robots.',
        )

    def test_student_list_shows_students_and_links_to_profile(self):
        response = self.client.get(reverse('personal_info:student_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SANTOS, Alex')
        self.assertContains(
            response,
            reverse('personal_info:student_detail', args=[self.student.pk]),
        )

    def test_student_list_shows_empty_state(self):
        self.student.delete()

        response = self.client.get(reverse('personal_info:student_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No students found yet.')

    def test_student_detail_shows_profile_sections(self):
        response = self.client.get(
            reverse('personal_info:student_detail', args=[self.student.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'STU-001')
        self.assertContains(response, 'Computer Engineering')
        self.assertContains(response, 'Enjoys building robots.')
        self.assertContains(response, 'Family &amp; Guardian')

    def test_missing_student_returns_404(self):
        response = self.client.get(
            reverse('personal_info:student_detail', args=[9999])
        )

        self.assertEqual(response.status_code, 404)
