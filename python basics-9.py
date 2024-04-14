basket = [1, 2, 3, 4, 5]

new_list1 = basket.append(100)
print(basket)
print(new_list1)

new_list2 = basket.insert(5, 100)
print(basket)
print(new_list2)

new_list3 = basket.extend([100, 101])
print(basket)
print(new_list3)

new_list4 = basket.extend([102])
basket.pop()
basket.pop(0)
basket.remove(4)
print(new_list4)

new_list6 = basket.clear
print(new_list6)