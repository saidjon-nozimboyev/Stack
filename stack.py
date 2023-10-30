from time import sleep
class Stack():

    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def append(self, vl:any)->None:
        "This function adds value to the list"
        self.size += 1
        self.data.append(vl)
    
    def empty(self)->bool:
        return self.size == 0
    
    def pop(self)->any:
        if not self.empty():
            self.size -= 1
            return self.data.pop()
        else:
            raise Exception("Stack is empty!")
        
    def top(self)->any:
        if not self.empty():
            return self.data[-1]
        else:
            raise Exception("Stack is empty!")
    
   
    @property
    def Size(self):
        return self.size

    def Clear(self):
        self.size = 0
        self.data.clear()


if __name__ == "__main__":
    st = Stack()      
    st.append("Hello")
    st.append("World")
    while not st.empty():
        print(st.pop(),end='')
