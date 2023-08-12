

try:
    1/0
except BaseException as error:
    print('An exception occurred: {}'.format(error))