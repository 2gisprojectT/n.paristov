__author__ = 'whitefoxnsk'


class Lion:
    def __init__(self, l_dict, status):
        if status == "":
            raise Exception("Empty status")
        self.status = status
        if l_dict == {}:
            raise Exception("Empty dict")
        self.l_dict = l_dict
        self.action = ""

    def result(self, text):
        if (text, self.status) not in self.l_dict:
            raise Exception("Wrong object")
        self.action = self.l_dict[(text, self.status)][0]
        self.status = self.l_dict[(text, self.status)][1]

if __name__ == '__main__':
    l_dict = {('antelope', 'fed'): ('Sleep,status change to hungry', 'hungry'),
              ('hunter', 'fed'): ('Run,status change to hungry', 'hungry'),
              ('tree', 'fed'): ('Watch,status change to hungry', 'hungry'),

              ('antelope', 'hungry'): ('Eat,status change to fed', 'fed'),
              ('hunter', 'hungry'): ('Run,still hungry', 'hungry'),
              ('tree', 'hungry'): ('Sleep,still hungry', 'hungry')}

    status = 'hungry'
    L = Lion(l_dict, status)

    while 1:
        print('Now lion is ' + L.status)
        print('Choose and enter one of this objects: antelope, hunter, tree')
        print('If you want quit,print exit')
        try:
            obj = input().lower()
            if obj == 'exit':
                break
            L.result(obj)
            print(L.action)
        except:
            print('Error, lion don\'t know object and action for him')