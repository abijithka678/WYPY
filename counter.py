name = 'abijith'
countere =0
dict={

}
for x in name:
    if x == 'a' and countere == 0 :
        value_a = name.count(x)
        dict_a = {
            x : value_a
        }
        dict.update(dict_a)
    elif x == 'b' and countere ==0 :
        value_b = name.count(x)
        dict_b = {
            x: value_b
        }
        dict.update(dict_b)
    elif x == 'i' and countere == 0:
        value_c = name.count(x)
        dict_c = {
            x: value_c
        }
        dict.update(dict_c)

print(value_a)
print(value_b)
print(value_c)
print(dict)
