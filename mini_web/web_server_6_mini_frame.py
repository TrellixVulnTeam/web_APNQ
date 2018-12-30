def application(env, start_response):
    start_response('200 OK', {("Content-Type", "text/html;charset=utf-8")})
    file_name = env["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return "Hello World!我爱你"


def index():
    return "index"


def login():
    return "login"
