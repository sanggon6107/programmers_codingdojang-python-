#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#module2

class Module2 :
    def __init__(self, first, second) :
        self.first = first
        self.second = second
        
    def plus(self) :
        
        result = self.first + self.second
        return result
        
if __name__ =="__main__" :
    print("__name__ ==\"__main__\"")