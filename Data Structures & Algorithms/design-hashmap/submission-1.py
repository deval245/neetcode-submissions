class MyHashMap:

    def __init__(self):
        self.freq = {}
        

    def put(self, key: int, value: int) -> None:
        self.freq[key] = value
        

    def get(self, key: int) -> int:
        if key in self.freq:
            return self.freq[key]
        return -1    
        

    def remove(self, key: int) -> None:
        if key in self.freq:
            del self.freq[key]