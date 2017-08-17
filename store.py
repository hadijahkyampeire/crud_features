class Store:
    def __init__(self):
        self.item = {}
        self.last_item_id = 0

    def add_item(self, item):
        self.last_item_id += 1
        self.item[self.last_item_id] = item
        item._id = self.last_item_id

    def delete_item(self, item_id):
        del self.item[item_id]

    def get_item(self, item_id):
        return self.item[item_id]

    def get_item(self):
        return self.item        
