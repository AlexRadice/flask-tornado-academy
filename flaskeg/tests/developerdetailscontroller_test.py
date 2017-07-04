from flaskeg.application import app
from flaskeg.developerdetailscontroller import DeveloperDetailsController
from unittest import TestCase
from flask.globals import g
from flask_login import current_user
from flask_principal import Identity, PermissionDenied

class DeveloperDetailsControllerTests(TestCase):
    "Test fixture for the DeveloperDetailsController class"

    def test_get(self):
        "Basic GET for new developer"
        with app.test_request_context('/developer'):
            controller = DeveloperDetailsController()
            response = controller.get()
            self.assertIsInstance(response, (str, unicode))
            self.assertIn('Favourite Fruit', response)


    def test_post_noauth(self):
        "POST without logging in"
        with app.test_request_context('/developer',
                                      method='POST',
                                      data={'name': 'Charlie Wyke',
                                            'cell': 'C',
                                            'favouritefruit': 'orange'
                                            }):
            g.identity = Identity(current_user.get_id())
            controller = DeveloperDetailsController()
            with self.assertRaises(PermissionDenied):
                response = controller.post()


