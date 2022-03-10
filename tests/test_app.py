from flask_testing import TestCase
from application import app, db
from application.models import Teams
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
                SECRET_KEY='SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLES=False 
                )
        return app

    def setUp(self):
        db.create_all()

        team1 = Teams(name="new team", description= "this new team")

        db.session.add(team1)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestCRUD(TestBase):

    def test_read_teams(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('new team', str(response.data))
        self.assertIn('this new team', str(response.data))

    def test_create_teams(self):
        response = self.client.post(
            url_for('create'),
            data=dict(name="created team", description="this is a create team"),
            follow_redirects=True
        )
        created_team = Teams.query.get(2)
        self.assertEqual(created_team.name, "created team")
        self.assertIn('created team', str(response.data))
        self.assertIn('this is a create team', str(response.data))

    def test_update_teams(self):
        response = self.client.post(
            url_for('update_team', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn("updated team", str(response.data))
        self.assertIn("this is an updated team", str(response.data))

    def test_delete_teams(self):
        response = self.client.post(
            url_for('delete', name="new team"),
            follow_redirects=True
        )
        self.assertNotIn("new team", str(response.data))