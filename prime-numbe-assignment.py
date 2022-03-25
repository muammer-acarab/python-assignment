prime_list = []
for i in range(1, 101):
    if(i>1):
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            prime_list.append(i)
print(prime_list)

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
