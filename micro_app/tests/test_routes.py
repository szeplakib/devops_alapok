import os
from flask_micro import create_app


def test_complex_task():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/complex_task' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/complex_task')
        assert response.status_code == 200
        assert b'This is the result of a computationally intensive task!' in response.data



def test_complex_task2():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/complex_task2' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/complex_task2')
        assert response.status_code == 200
        assert b'This is the result of another computationally intensive task!' in response.data
