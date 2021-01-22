from unittest.mock import Mock, patch

from django.test import TestCase

from simple_app.middleware import LogAllRequestsMiddleware


class TestLogAllRequestsMiddleware(TestCase):

    def setUp(self):
        self.request = Mock()
        self.request.GET.dict = Mock(return_value={'test_get': 'test_get'})
        self.request.POST.dict = Mock(return_value={'test_post': 'test_post'})
        self.respone = Mock()
        self.middleware = LogAllRequestsMiddleware()

    @patch('simple_app.middleware.logger')
    def test_processing_response(self, logger: Mock):
        result = self.middleware.process_response(
            self.request, self.respone
        )
        self.assertIs(self.respone, result)

    def test_get_params(self):
        expected_params: dict = {
            'test_get': 'test_get',
            'test_post': 'test_post'
        }
        params: dict = self.middleware._get_params(self.request)
        self.assertEquals(expected_params, params)

    @patch('simple_app.middleware.logger')
    def test_logging(self, logger: Mock):
        self.middleware.process_response(
            self.request, self.respone
        )
        logger.info.assert_called_once()
