from django.test import TestCase
from django.urls import reverse

from simple_app.forms import SimpleForm


class TestIndexView(TestCase):

    def test_method_get_receive_form(self):
        resp = self.client.get(reverse('simple_app:index'))
        form = resp.context.get('form')
        self.assertIsInstance(form, SimpleForm)

    def test_method_get_uses_correct_template(self):
        resp = self.client.get(reverse('simple_app:index'))
        self.assertTemplateUsed(resp, 'simple_app/index.html')

    def test_method_post_return_redirect(self):
        resp = self.client.post(
            reverse('simple_app:index'),
            {'email': 'test@test.ru'},
        )
        self.assertRedirects(
            resp, reverse('simple_app:index'),
            status_code=302, target_status_code=200,
            msg_prefix='', fetch_redirect_response=True,
        )


class TestApiView(TestCase):

    def test_method_get_return_status_code_404(self):
        resp = self.client.get(reverse('simple_app:api'))
        self.assertEqual(resp.status_code, 404)

    def test_method_post_with_wrong_params_return_status_code_400(self):
        resp = self.client.post(reverse('simple_app:api'))
        self.assertEqual(resp.status_code, 400)

    def test_method_post_with_right_params_return_status_code_200(self):
        resp = self.client.post(f"{reverse('simple_app:api')}?method=ping")
        self.assertEqual(resp.status_code, 200)
