# set= collection which is unordered, un-indexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
dish_ware = utensils.union(dishes)
for x in dish_ware:
    print(x)
# print(utensils)
