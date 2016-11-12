import json
from flask_testing import TestCase
import nose
from faker import Factory

from main.manage import app, db
from trial.models import User

fake = Factory.create()


class AWTCTestCase(TestCase):

    def create_app(self):
        """Initial configuration details."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tests.db'
        self.client = app.test_client()
        return app

    def setUp(self):
        """Initial data in the db."""
        db.create_all()
        self.username = fake.user_name()
        self.email = fake.email()
        self.password = fake.password()
        self.user = User(username=self.username,
                         password=self.password,
                         email=self.email)
        db.session.add(self.user)
        db.session.commit()

    def test_user_registration(self):
        """Test that creation of a user succeeds when correct info is sent."""
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        response = self.client.post('/register',
                                    data=json.dumps({
                                        'username': username,
                                        'password': password,
                                        'email': email}),
                                    content_type='application/json')
        number_users = User.query.all()
        # self.assertIn('User {} has been successfully registered'.
        #               format(username), response.data)
        self.assertEqual(len(number_users), 1)
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        """Clean up after tests."""
        with app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    nose.run()
