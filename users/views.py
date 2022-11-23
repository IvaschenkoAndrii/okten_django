from rest_framework.views import APIView
from rest_framework.response import Response
import json

users = []


def gen():
    count = 0
    while True:
        count += 1
        yield count


g = gen()


class UserLisrCreate(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def gen(self):
        count = 0
        while True:
            count += 1
            yield count

    def get(self, *args, **kwargs):
        try:
            with open('users/users.json', 'r') as file:
                users = json.load(file)
        except Exception as err:
            print('no found')
        return Response(users)

    def post(self, *args, **kwargs):
        id_user = str(next(g))
        user = {'id': id_user, 'name': self.request.data['name'], 'age': self.request.data['age']}
        users.append(user)
        print(users)

        try:
            with open('users/users.json', 'w') as file:
                json.dump(users, file)
        except Exception as err:
            print(err)
        return Response(user)


class UserRetrieveUpdateDelete(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.users = users

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            with open('users/users.json', 'r') as file:
                self.users = json.load(file)
                try:
                    user=self.users[pk-1]
                except IndexError:
                    return Response ('Not Found')
        except Exception as err:
            print('not found')
        return Response(user)
