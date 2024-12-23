# 11mt wall big brick is 3mt and small brick size is 1
# how many big_bricks and small_bricks need
target=int(input("Enter Target in Mts"))
big_brick_size=int(input("Big Brick Size in mts"))
small_brick_size=int(input("Small Brick Size in Mts"))
tbigbricks=target//big_brick_size
tsmallbricks=(target%big_brick_size)
print("Big Bricks Need is " + str(tbigbricks))
print("Small Bricks Need is " + str(tsmallbricks))









