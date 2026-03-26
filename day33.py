info={'name':'farhan','age':18,'city':'lahore','eligibile':True}
print(info)
# print(info['name'])
print(info.keys())
for key in info.keys():
    # print(info[key])
    print(f'The corresponding to the value {key} is {info[key]}')