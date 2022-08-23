# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# from collections import Counter
# k=Counter(my_dict)
# high=k.most_common(3)
# for i in high:
    # print(i[1])
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]   
p =0
for items in student:
        if items['success'] == True:
            p+= 1
print(p)