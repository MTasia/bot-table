class Date:
    def __init__(self):
        self.entry = False

    def set_status(self, status):
        self.entry = status

    def get_status(self):
        return self.entry


date_entry = Date()
