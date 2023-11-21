# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single pa
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        # self.collection = collection
        self.items_per_page = items_per_page

        self.i_count = len(collection)
        self.p_count = int(self.i_count / self.items_per_page) if not (self.i_count / self.items_per_page)>int(self.i_count / self.items_per_page) else int(self.i_count / self.items_per_page)+1
        
        self.is_last_page_full = True if not self.i_count % items_per_page else False
        self.redundancy = self.items_per_page if self.is_last_page_full else self.i_count % items_per_page
    # returns the number of items within the entire collection
    def item_count(self):
        return self.i_count
    
    # returns the number of pages
    def page_count(self):
        return self.p_count
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.p_count or page_index < 0:
            return -1
        return self.items_per_page if page_index != self.p_count - 1 else self.redundancy
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0:
            return -1
        return int(item_index / self.items_per_page) if item_index <= self.i_count - 1 else -1

if __name__ == "__main__":
    helper = PaginationHelper(['a','b','c','d','e','f'],4)
    print(helper.page_count())  # 应该等于 2
    print(helper.item_count())  # 应该等于 6
    print(helper.page_item_count(0))  # 应该等于 4
    print(helper.page_item_count(1))  # 最后一页 - 应该等于 2
    print(helper.page_item_count(2))  # 应该等于 -1，因为页面无效

    # page_index接受一个项目索引并返回其所属的页面
    print(helper.page_index(5))  # 应该等于 1（从零开始的索引）
    print(helper.page_index(2))  # 应该等于 0
    print(helper.page_index(20))  # 应该等于 -1
    print(helper.page_index(-10))  # 应该等于 -1，因为负索引无效