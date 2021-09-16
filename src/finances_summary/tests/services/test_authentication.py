import pytest
from starlette.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT,
                              HTTP_422_UNPROCESSABLE_ENTITY)
from mongoengine import connect, Q
from finances_summary.services.authentication import register, login as login_user
from finances_summary.models.mongo.users import Users
from finances_summary.settings import MONGO_CONN_URI

connect(host=MONGO_CONN_URI)


@pytest.mark.parametrize('username,password,email',
                         [('testuser', 'testpwd', 'test@email.test'),
                          ('testcharacters', '1n@#$^&)!@<>o23', 'test@testtt.test'),
                          ('test123user', 'testpwd', 'number42@qwerty.test')])
def test_register_user_success(username: str, password: str, email: str) -> None:
    response = register(username, password, email)
    # Delete created user after we get response.
    assert response.status_code == HTTP_200_OK


@pytest.mark.parametrize('username,password,email',
                         [('bad$#@name', 'testpwd', 'badname@email.test'),
                          ('testempty', '', 'testempty@test.test'),
                          ('testemptyemail', 'emptyemail', ''),
                          ('testwrongemail', 'testemail', 'testemail.test'),
                          ('testname', 'emptyname', 'emptyname@test')])
def test_register_user_fail(username: str, password: str, email: str):
    response = register(username, password, email)
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize('login,password', [('testuser', 'wrongpwd'),
                                            ('wrongname', '1n@#$^&)!@<>o23'),
                                            ('notexist@email.email', 'testpwd')])
def test_login_fail(login: str, password: str):
    response = login_user(login, password)
    # Delete created user after we get response.
    assert response.status_code == HTTP_401_UNAUTHORIZED


# Use same users from register success test.
@pytest.mark.parametrize('login,password', [('testuser', 'testpwd'),
                                            ('test@testtt.test', '1n@#$^&)!@<>o23'),
                                            ('test123user', 'testpwd')])
def test_login_success(login: str, password: str) -> None:
    response = login_user(login, password)
    # Delete created user after we get response.
    Users.objects(Q(username=login) | Q(email=login)).first().delete()
    assert response.status_code == HTTP_200_OK
