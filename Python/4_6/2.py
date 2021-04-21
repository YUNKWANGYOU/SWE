import sys
sys.stdout.write('2015112173 유윤광\n')

fruitlist = ['banana','Orange','Kiwi','cherry']
print('Original list : ',fruitlist)

fruitlist.reverse()
print("reverse() -> ",fruitlist)

fruitlist.sort()
print("sort() -> ",fruitlist)

fruitlist.sort(key = str.lower)
print("sort(key=str.lower) -> ",fruitlist)