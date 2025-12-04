class Tag:
    """Stub for bs4.element.Tag"""
    def __init__(self):
        pass

    def find_all(self, *args, **kwargs):
        return []

    def find(self, *args, **kwargs):
        return None

    def get(self, key, default=None):
        return default

    def select(self, selector):
        return []

    def decompose(self):
        pass

    @property
    def descendants(self):
        return []

    @property
    def name(self):
        return None


class BeautifulSoup(Tag):
    def __init__(self, text, parser):
        super().__init__()
