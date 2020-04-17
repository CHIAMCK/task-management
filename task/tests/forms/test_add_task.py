from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from company.models import Company
from task.forms import AddTaskForm
from team_member.models import TeamMember

User = get_user_model()


# Create your tests here.
class TestAddTaskForm(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='password123'
        )

        self.company = Company.objects.create(
            name='test company',
            email='test@gmail.com'
        )

        self.team_member = TeamMember.objects.create(
            user=self.user,
            name='test team member',
            email=self.user.email,
            company=self.company
        )

        self.task_form_data = {
            'title': 'test task',
            'description': '',
            'status': 1,
            'due_date': '',
            'assigned_to': 2
        }

    def test_form_save(self):
        factory = RequestFactory()
        request = factory.post('/')
        data = self.task_form_data

        form = AddTaskForm(data=data, request=request)
        print(form.errors)
        self.assertTrue(form.is_valid())
