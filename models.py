from werkzeug.security import generate_password_hash, check_password_hash

from manage import db


class User(db.Model):
    """Set up user attributes definition."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128))

    def hash_password(self, password):
        """Return password as hash to be stored in DB."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Verify the password entered as the user's returns True if it is."""
        return check_password_hash(self.password, password)


if __name__ == "__main__":
    db.create_all()
