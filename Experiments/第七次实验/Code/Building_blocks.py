class Block:
    # Good Luck!
    def __init__(self,lst):
        self.width = lst[0]
        self.length = lst[1]
        self.height = lst[2]
    
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.get_width() * self.get_length() * self.get_height()
    
    def get_surface_area(self):
        return 2 * (self.get_width() * self.get_length() + self.get_length() * self.get_height() + self.get_width() * self.get_height())