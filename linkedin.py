"""Helper functions for using LinkedIn API and OAuth."""

import os
import requests

OAUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
ACCESS_TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
REQUEST_DATA_URL = "https://api.linkedin.com/v1/people/~?format=json"


def get_auth_code():
    """Request auth code from LinkedIn API."""

    pass


def get_access_token():
    """Exchange auth code from get_auth_code for user Access Token."""

    pass


def get_user_data():
    """Use Access Token to make authenticaled API requests from LinkedIn."""

    pass
