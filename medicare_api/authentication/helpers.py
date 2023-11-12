from rest_framework.authentication import TokenAuthentication


class CustomAuth(TokenAuthentication):
    keyword = "Bearer"
