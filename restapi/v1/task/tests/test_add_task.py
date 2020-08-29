
from rest_framework.test import APITestCase
from team_member.models import TeamMember
from company.models import Company

# docker-compose exec web python manage.py test restapi/v1/

# able to add task
# add task with missing field data
# add task without login


class AddTaskTests(APITestCase):
    def setUp(self):
        self.tm = TeamMember.objects.create(name='foo', email='test@gmail.com')
        self.company = Company.objects.create(name='company ABC', email='companyABC@gmail.com')
        self.tm.company = self.company
        print(self.tm.__dict__)

    def test_create_task(self):
        # setup
        data = {'username': 'foo', 'password': 'Abcd123!'}
        self.client.post('/sec/api/v1/login', data)

        # execution
        data = {
            'title': 'testing',
            'description': '123',
            'status': 1,
            'assigned_to': 1
        }
        response = self.client.post('/sec/api/v1/tasks', data, format='json')

        # assertion

        print(response.status_code)
        assert response.status_code == 201
