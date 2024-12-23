import os
from flask_main import create_app


def test_hello():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/hello' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/hello')
        assert response.status_code == 200
        assert b"Hello" in response.data



def test_square():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/square' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/square/2')
        assert response.status_code == 200
        assert b"4" == response.data
        response = test_client.get('/square/2.2')
        assert response.status_code == 200
        assert b"4.84" == response.data
        response = test_client.get('/square/asd')
        assert response.status_code == 200
        assert b"Numbers are expected, you provided the following: asd" == response.data
