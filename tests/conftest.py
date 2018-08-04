import pytest
from app.api import app as application
from app.api import db


@pytest.fixture(scope='session')
def app(request):
    ctx = application.app_context()
    ctx.app.config['DEBUG'] = True
    ctx.app.config['TESTING'] = True
    ctx.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return application


@pytest.fixture(scope='session')
def test_client(app):
    return app.test_client()


@pytest.fixture(scope='session', autouse=True)
def build_db(app):
    db.create_all()


@pytest.fixture(scope='function', autouse=True)
def rollback(app, request):
    def fin():
        db.drop_all()
        db.create_all()
    request.addfinalizer(fin)
