# Creating an own range Function

class my_range:

    def __init__(self,start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return my_range_iterator(self)



class my_range_iterator:
    def __init__(self,iterable_obj):  # this iterbale object has both start and end as it an object of my_range class
        self.iterable = iterable_obj

    def __iter__(self):      # iterators iterator is same as we discussed

        return self 
    
    def __next__(self):
         if self.iterable.start >= self.iterable.end:
             raise StopIteration
         
         current = self.iterable.start
         self.iterable.start +=1
         return current
    



for i in my_range(1,20):
    print(i)