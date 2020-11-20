# while True: print('Hello world')

# try:
#     result = 100 / 0
# except ZeroDivisionError as e:
#     print(e)


# try:
#     result = 5 * not_defined
# except NameError as e:
#     print(e)


# try:
#     result = '2' + 2
# except TypeError as e:
#     print(e)


# try:
#     raise Exception('Some Error Occured')
# except Exception as e:
#     print(e)


# try:
#     result = '2' + 1
#     zero_error = 100 / 0
#     raise Exception('Some Error Occured')
# except (ZeroDivisionError, TypeError, NameError, Exception) as e:
#     print(f'Erro occured, {e}')


# try:
#     print('No Exception')
# except Exception as e:
#     print('I don\'t catch')
# else:
#     print('always I am here')


# try:
#     raise Exception({'message': 'Unauthorized', 'status': 401})
#     # raise ValueError
# except Exception as e:
#     print(type(e))
#     print(e.args)

# try:
#     raise NameError('Mongo Connection Error')
#     # try:
#     # except NameError as e:
#     #     print('caught Name Error', e)
#     #     raise ValueError('MySQL Error')
# except NameError as e: raise
# except Exception as e:
#     print('DB Connection: ', e)
# finally:
#     print('final call')

# print('this is fine')

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise
# finally:
#     print('Cleaning up...')


def connect():
    try:
        try:
            print('Attempting connection to mongodb')
            raise NameError('MongoDB')
        except NameError as e:
            print('Attempting connection to MySQL')
            raise ValueError('MySQL')
        except Exception as e:
            print('DB Connection Error', e)
    except Exception as e:
        print('Database connection unsuccessfull')



connect()
print('Server started')


    