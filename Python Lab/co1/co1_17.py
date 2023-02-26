'''
Sort dictionary in ascending and descending order.  
'''

d = {5:'apple',2:'orange',7:'grapes',1:'guava'}
asc_key = sorted(d.items())
desc_key = sorted(d.items(),reverse=True)

print(dict(asc_key))
print(dict(desc_key))

asc_val = sorted(d.items(),key = lambda value : value[1])
desc_val =sorted(d.items(), key = lambda value : value[1],reverse=True)

print(dict(asc_val))
print(dict(desc_val))
