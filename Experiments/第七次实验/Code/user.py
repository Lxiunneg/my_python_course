class User:
    def __init__(self):
        self.ranklist = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.index = 0
        self.rank = self.ranklist[self.index]
        self.progress = 0

    def inc_progress(self,proRank):
        if proRank < -8 or proRank > 8 or proRank == 0:
            raise Exception('Error')

        if proRank < 0:
            proRank += 8
        else:
            proRank += 7
        
        if proRank == self.index:
            self.progress += 3
        elif proRank < self.index:
            if self.index - proRank < 2 and self.index - proRank > 0:
                self.progress += 1
        elif proRank > self.index:
            d = proRank - self.index
            self.progress += 10 * d * d
    
        if self.progress >= 100 and self.rank != 8:
            # print(self.progress)
            p = int(self.progress / 100)
            # print(p)
            self.progress %= 100
            self.index += p
            if self.index >= 15:
                self.index = 15
            self.rank = self.ranklist[self.index]

        if self.rank == 8:
            self.progress = 0


if __name__ == "__main__":
    user = User()
    print(user.rank) # => -8
    print(user.progress) # => 0
    user.inc_progress(-7)
    print(user.progress) # => 10
    user.inc_progress(-5) # will add 90 progress
    print(user.progress) # => 0 # progress is now zero
    print(user.rank) # => -7 # rank was upgraded to -7
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    print(user.rank)
    print(user.progress)