from re import sub


def given_string(string):
    if (string.startswith('q')):
        print('q found', string)

def filter_users_subscribed(users):
    subscribed_user = []
    for user in users:
        if(user['is_subscribed']):
            subscribed_user.append(user)
    return subscribed_user


list_of_strings = ['one','two','three','quack']
string_given = 'i was given this string'

for string in list_of_strings:
    given_string(string)


users = [
    {
        'username': 'tyler',
        'is_subscribed': False,
        'age': 12
    },
    {
          'username': 'ty',
        'is_subscribed': True,
        'age': 16
    },
    {
        'username': 'duck',
        'is_subscribed': True,
        'age': 14
    }
]

subscribed_users = filter_users_subscribed(users)
print(subscribed_users)