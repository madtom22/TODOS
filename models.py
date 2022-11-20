import json

class Todos:
    def __init__(self):
        try:
            with open("todos.json","r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []


    def all(self):
        return self.todos


    def get(self, id):
        todo = [ todo for todo in self.all() if todo['id'] == id]
        if todo:
            return todo[0]
        return self.todo[id]


    def create(self, data):
        data.pop('csrf.token')
        self.todos.append(data)


    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)


    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False


    def delete(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False


todos = Todos()
