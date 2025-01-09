# def ma_fonction(**kwargs):
        
#         print('ma variable, est', kwargs)

# ma_fonction(quatre =4, trois=3, deux=2, un=1)

# def somme(a, b):
#         return a+b,a,b



# print( somme(5,4))
# a=0
# def fonction_1():
        
#         print('fontion_1, a=', a)

# def fonction_2():
#         a=2
#         print('fonction_2  a=', a)

# print(a)

# fonction_1()
# fonction_2()
#pour faire une boucle de 1 à n
def simple_range(n):
        l = []
        i = 0
        
        while i < n:
                l.append(i)
                i += 1

        return l

print(simple_range(5))

