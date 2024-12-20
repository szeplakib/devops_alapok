import os
from flask_micro import create_app


def complex():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/complex' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/complex')
        assert response.status_code == 200
        assert b'This is the result of a computationally intensive task!' in response.data



def complex2():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/complex' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/complex2')
        assert response.status_code == 200
        assert b'This is the result of another computationally intensive task!' in response.data