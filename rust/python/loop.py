numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = {'mangoes':20,'bananas':40,'jackfruit':30, 'oranges':70,'pineapple':45,'tangerine':55}

greater = {}
for fruit in fruits:
    if (fruits[fruit]) > 50:
        greater.update({fruit:fruits[fruit]})


print(greater)

greater = {
    fruit:fruits[fruit] 
    for fruit in fruits 
    if fruits[fruit] > 50}
print(greater)





