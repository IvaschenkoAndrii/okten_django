from rest_framework.views import APIView
from rest_framework.response import Response
import json

with open('users/users.json', 'r') as file:
    users = json.load(file)


# users = []


def gen():
    count = int(users[-1]['id']) if users else 0
    # count = 0
    while True:
        count += 1
        yield count


g = gen()


class UserLisrCreate(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

        try:
            with open('users/users.json', 'w') as file:
                json.dump(users, file)
        except Exception as err:
            print(err)
        return Response(user)


class UserRetrieveUpdateDelete(APIView):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.users = users

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            with open('users/users.json', 'r') as file:
                users = json.load(file)
                try:
                    for i in range(len(users)):
                        if int(users[i]['id'])==pk:
                            user = users[i]
                except IndexError:
                    return Response('Not Found')
        except Exception as err:
            print('not found')
        return Response(user)
