''' Quadratic Probing '''

class Hashing:
    def __init__(self,c1,c2,m):
        self.hashtable = []
        for i in range(m):
            self.hashtable.append(None)     
        self.c1 = c1
        self.c2 = c2
        self.m = m


    def store_data(self, data):
        probe = 0
        while(True):
            h_k_i = self.hash((hash(data) + self.c1*probe + self.c2 * probe ** 2))
            if self.hashtable[h_k_i] == None:
                break

            probe = probe + 1
            if probe == self.m-1:
                return("Hash table is full.")
        
        self.hashtable[h_k_i] = data

    
    def hash(self, data):
        return (data % self.m)

    
    def display_hashtable(self):
        print("[", end="")
        for i in range(m):
            print(self.hashtable[i], end=", ")
        print("]", end="")




c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
	A.store_data(i)
print(A.display_hashtable())