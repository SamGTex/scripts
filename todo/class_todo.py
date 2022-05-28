class ToDo:
    def __init__(self, name: str):
        self.tasks = []
        self.name = name

    def get(self):
        return self.tasks
    
    def size(self):
        return len(self.tasks)
        
    def add(self, task: str):
        self.tasks.append(task)
    
    def show(self):
        print('To Do:')
        for i, task in enumerate(self.tasks):
            print(f'{i+1}. {task}')
    
    def delete(self, num: int):
        del self.tasks[num-1]

    def save_to_file(self):
        with open(f'/home/gtex/scripts/todo/data/{self.name}.txt', 'w') as f:
            for task in self.tasks:
                f.write(f'{task}\n')
    def read_in(self):
        with open(f'/home/gtex/scripts/todo/data/{self.name}.txt') as f:
            self.tasks = [line.rstrip() for line in f]

if __name__ == '__main__':
    today = ToDo('today')
    
    #today.add('Spazieren')
    #today.add('Essen')
    #today.add('Im Kreis laufen')
    #today.show()
    #today.save_to_file()

    today.read_in()
    today.show()