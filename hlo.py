class myclass:
    def __init__(self,value):
        self._value=value
    
    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new):
        self._value=new/10
        
obj=myclass(10)
obj.ten_value=78
print(obj.ten_value)