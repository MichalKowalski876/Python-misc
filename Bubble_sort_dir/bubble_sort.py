import json


def get_list():
    fh = open("list.json")
    list_sort = json.load(fh)

    list_type(list_sort)


def list_type(list_sort):
    #  for i in range(len(list_sort)):
    #    if type(list_sort) == str:
    #         mix_sort(list_sort)
    #        print('str')
    #   else:
    int_sort(list_sort)

def check_sort(list_sort):
    for var in range(len(list_sort)):
        if(True):
            pass

##list.insert(index, variable)
def int_sort(list_sort):
    for var in range(len(list_sort) - 1):
        if (list_sort[var] > list_sort[var + 1]):
            list_sort.insert(var + 1, list_sort[var])
            list_sort.pop(var)



def mix_sort(list_sort):
    pass


if __name__ == '__main__':
    get_list()
