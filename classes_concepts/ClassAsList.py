class SuperList(list):
    def __len__(self):
        return 5
    def __call__(self):
        print(self)

list1= SuperList()
list1.append(5)
list1.insert(0,'Prabesh')
list1()

