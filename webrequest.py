import requests

'''
This method autologin you in the website.
'''
def autologin(user, password, isNextWeek):
    urlLogin = "http://156.35.95.28:8081/identificarse"

    if isNextWeek:
        urlHorario = "http://156.35.95.28:8081/proponer-horario"
    else:
        urlHorario = "http://156.35.95.28:8081/horario"

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    login_data = {
        'email': user,
        'password': password
    }

    with requests.Session() as s:
        s.post(urlLogin, data=login_data, headers=headers)
        r = s.get(urlHorario)
        return r.iter_lines()