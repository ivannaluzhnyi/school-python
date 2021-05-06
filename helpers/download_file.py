

def encode_path(name):
    return "_".join(str(name).split('/'))


def decode_path(name):
    return "/".join(str(name).split('_'))


def get_filename(name, symbol="_"):
    return str(name).split(symbol)[-1]
