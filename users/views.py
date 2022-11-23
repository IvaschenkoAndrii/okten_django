from rest_framework.views import APIView
from rest_framework.response import Response
import json


class UserLisrCreate(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.users = []

    def get(self, *args, **kwargs):
        try:
            with open('users/users.json', 'r') as file:
                self.users = json.load(file)
        except Exception as err:
            print(err)
        return Response(self.users)

    def post(self, *args, **kwargs):
        try:
            with open('users/users.json', 'w') as file:
                user = self.request.data
                self.users.append(user)
        except Exception as err:
            print(err)
        return Response(user)
