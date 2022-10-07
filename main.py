whole = ""
while True:
    message = input()
    if message == "":
        break
    whole = f'{whole}{message}'
print(f'The whole message is :\n{whole}')

