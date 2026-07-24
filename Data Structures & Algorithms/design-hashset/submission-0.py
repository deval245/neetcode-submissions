class MyHashSet:

    def __init__(self):
        self.freq = set()
        

    def add(self, key: int) -> None:
        if key not in self.freq:
            self.freq.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.freq:
            self.freq.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.freq:
            return True
        return False