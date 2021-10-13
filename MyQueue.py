class MyQueue:

    def __init__(self):
        self.data = []

    def pop(self):
        data = self.data[0]
        self.data.remove(data)
        return data

    def append(self, data) -> None:
        self.data.append(data)
