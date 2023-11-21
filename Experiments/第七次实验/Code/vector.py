class Vector:
  # TODO: Finish the Vector class.
    def __init__(self,list):
        self.vector = list
        self.len = len(list)
        
    def ThrowErr(self):
        raise Exception("抛出一个异常") 
            
    def __getitem__(self, index):
        return self.vector[index]
    
    def __len__(self):
        return self.len
    
    def add(self,vector):
        if self.len != len(vector):
            self.ThrowErr()
        temp_list = []
        for i in range(self.len):
            temp = self.vector[i] + vector[i]
            temp_list.append(temp)
        return Vector(temp_list)
    
    def subtract(self,vector):
        if self.len != len(vector):
            self.ThrowErr()
        temp_list = []
        for i in range(self.len):
            temp = self.vector[i] - vector[i]
            temp_list.append(temp)
        return Vector(temp_list)
    
    def dot(self,vector):
        if self.len != len(vector):
            self.ThrowErr()
        temp_list = []
        for i in range(self.len):
            temp = self.vector[i] * vector[i]
            temp_list.append(temp)
        return sum(temp_list)
    
    def norm(self):
        for i in range(self.len):
            self.vector[i] = self.vector[i] ** 2
        return (sum(self.vector)) ** 0.5
    
    # def equals(self,vector):
    #     if self.len != len(vector):
    #         return False
    #     for i in range(self.len):
    #         if self.vector[i] != vector[i]:
    #             return False
    #     return True
        
    def equals(self, vector):
        if self.len != len(vector):
            return False
        return all(self.vector[i] == vector[i] for i in range(self.len))

if __name__ == '__main__':
    a = Vector([1,2,3])
    b = Vector([1,2,2])

    print(a.equals(b))