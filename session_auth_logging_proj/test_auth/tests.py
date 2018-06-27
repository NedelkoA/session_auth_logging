from django.test import TestCase


class TaskViewTest(TestCase):
    def test_view(self):
        r = self.client.get()
