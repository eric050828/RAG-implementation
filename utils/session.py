from json import loads, dumps


def save_session(data: dict):
    with open(".config\\session.json", "w") as f:
        f.write(dumps(data))
        
def load_session():
    with open(".config\\session.json", "r") as f:
        return loads(f.read())