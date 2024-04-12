amazon_cart= ["football", "boots", "stockings", "skins", "box", "bottles"]
print(amazon_cart[0])
print(amazon_cart)
print(amazon_cart[0:1:2])
amazon_cart[3] = "laptop"
print(amazon_cart)
new_cart = amazon_cart[0:3]
new_cart[2] = "gum"
print(new_cart)
new_cart = amazon_cart[:]
print(new_cart)
new_cart[5] = "gumballs"
print(new_cart)
# this is known as a list
# for an eg l1 = [1, 2, 3, 4]
# or l2 = [a, b, c, d]
# or l3 = [a, 2, true, 3] even booleans can be added in lists