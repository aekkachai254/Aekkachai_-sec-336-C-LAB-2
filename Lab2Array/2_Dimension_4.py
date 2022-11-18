# exercise 4
arr_2d = [["numberId","Name","Count","Status"]]
print(len(arr_2d))
arr_2d.append([1,"Rubber",0,"Out of stock"])
arr_2d.append([2,"Ruler",5,"In stock"])
arr_2d.append([3,"Pencil",1,"In stock"])
print(arr_2d)

# exercise 5
arr_2d.append([4,"Pen",10,"In stock"])
arr_2d.append([5,"Colour pencil",5,"In stock"])
arr_2d.append([6,"A4 Paper",0,"Out of stock"])

def buy_and_update(buy, cnt):
    for i in range(len(arr_2d)):
        if arr_2d[i][1] == buy and arr_2d[i][3] == 'In stock':
            arr_2d[i][2] -= cnt
            if arr_2d[i][2] == 0:
                arr_2d[i][3] = 'Out of stock'
            print(f'{buy} is sold.')
            print(f'Update {buy}\'s stock : {arr_2d[i]}')
            break
        elif arr_2d[i][1] == buy and arr_2d[i][3] == 'Out of stock':
            print(f'{buy} is Out of stock')
            break

print('\nIn stock')
for i in range(len(arr_2d)):
    if arr_2d[i][3] == 'In stock':
        print(arr_2d[i])

print('\nWhere out of stock')
for i in range(len(arr_2d)):
    if arr_2d[i][3] == 'Out of stock':
        print(arr_2d[i])

print('\nbuy 1 ruler')
buy_and_update('Ruler', 2)
print('\nbuy 1 pencil')
buy_and_update('Pencil', 1)
print('\nbuy 2 pens')
buy_and_update('Pen', 2)
print('\nbuy 1 colour pencil')
buy_and_update('Colour pencil',1)