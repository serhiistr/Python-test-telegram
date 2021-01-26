# Что выведет код?

x = True
y = False
z = False

if not x or y:                          #not X = False и Y = False
    print(1)
elif not x or (not y and z):              # not X = False или (not Y = True и z = False)
    print(2)
elif not x or y or (not y and x):         # (not X = False) или (Y = False) или (not Y = True и X = True)
    print(3)
else:
    print(4)

# Стоит помнить, что NOT имеет наивысший приоритет, потом идет AND, затем OR
# Выйдет из цикла когда будет True в результате