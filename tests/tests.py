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
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = app.test_client()
        return app

    def setUp(self):
        """Initial data in the db."""
        db.create_all()
        self.username = fake.username()
        self.email = fake.email()
        self.password = fake.password()
        self.user = User(username=self.username,
                         password=self.password,
                         email=self.email)
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """Clean up after tests."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # def test_new_successful_user_register(self):


if __name__ == '__main__':
    nose.run()
