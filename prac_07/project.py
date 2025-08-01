import datetime

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage >= 100

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage != "":
            self.completion_percentage = int(new_percentage)
        if new_priority != "":
            self.priority = int(new_priority)
