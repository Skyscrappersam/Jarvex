PROVIDERS = {}


def register(name, provider):

    PROVIDERS[name] = provider


def get_provider(name):

    return PROVIDERS.get(name)


def list_providers():

    return list(PROVIDERS.keys())