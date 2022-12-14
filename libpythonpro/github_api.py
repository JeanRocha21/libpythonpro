import requests


def buscar_avatar(usuario):
    '''

    Busca o avatar do usuario no Github

    :param usuario: str com o nome do usuario
    :return: str com link do avatar
    '''

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('jeanrocha21'))