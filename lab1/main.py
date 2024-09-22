class SparseSet:
    def __init__(self, maxV, cap):
        self.sparse = [None] * (maxV + 1)             # Зберігає індекс ел. у масиві dense[]
        self.dense = [None] * cap                     # Зберігає поточні елементи
        self.capacity = cap                        # max. потужність множини
        self.maxValue = maxV                       # max. значення елементу (елементи є 0...maxValue)
        self.n = 0                                 # поточний розмір

    
    def search(self, x):
        if x > self.maxValue or x < 0:
            return -1
        
        if self.sparse[x] != None:
            return True

 
        # if self.sparse[x] < self.n and self.dense[self.sparse[x]] == x:
        #     return self.sparse[x]
 
        return -1
 

    def insert(self, x):
        if x > self.maxValue:
            return
        if self.n >= self.capacity:
            return
        if self.search(x) != -1:
            return
 
        self.dense[self.n] = x
 
        self.sparse[x] = self.n
 
        self.n += 1
 
  
    def deletion(self, x):
        if self.search(x) == -1:
            return
 
        temp = self.dense[self.n - 1] 
        self.dense[self.sparse[x]] = temp 
        self.sparse[temp] = self.sparse[x] 
 
        self.n -= 1
    

    def Clear(self):
        self.n = 0
 
    
    def print_set(self):
        for i in range(self.n):
            print(self.dense[i], end=' ')
        print()


    def setUnion(self, set2):
       
        uCap = self.n + set2.n
        uMaxVal = max(self.maxValue, set2.maxValue)
         
        union_set = SparseSet(uMaxVal, uCap)
 
        for i in range(self.n):
            union_set.insert(self.dense[i])
 
        for i in range(set2.n):
            union_set.insert(set2.dense[i])
 
        return union_set
    

    def intersection(self, s):
        iCap = min(self.n, s.n)
        iMaxVal = max(s.maxValue, self.maxValue)
 
        result = SparseSet(iMaxVal, iCap)
        if self.n < s.n:
            for i in range(self.n):
                if s.search(self.dense[i]) != -1:
                    result.insert(self.dense[i])
        else:
            for i in range(s.n):
                if self.search(s.dense[i]) != -1:
                    result.insert(s.dense[i])
 
        return result


    def setdifference(self, other):
        result = SparseSet(self.maxValue, self.capacity)
        for i in range(self.n):
             if other.search(self.dense[i]) == -1:
                result.insert(self.dense[i])
        return result
    

    def symmetric_difference(self, other):
        result = SparseSet(self.maxValue, self.capacity)
        for i in range(self.n):
            if other.search(self.dense[i]) == -1:
                result.insert(self.dense[i])
        for i in range(other.n):
            if self.search(other.dense[i]) == -1:
                result.insert(other.dense[i])
        return result

    
    def issubset(self, other):
        for i in range(self.n):
            if other.search(self.dense[i]) == -1:
                return False
        return True
    
#
#
#
