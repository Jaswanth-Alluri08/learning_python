Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={"year":2026,"month":9,"date":28}
>>> a.keys()
dict_keys(['year', 'month', 'date'])
>>> a.values()
dict_values([2026, 9, 28])
>>> a.items()
dict_items([('year', 2026), ('month', 9), ('date', 28)])
>>> a["year"]
2026
>>> a["month"]
9
>>> a.get("year")
2026
>>> a
{'year': 2026, 'month': 9, 'date': 28}
>>> a={"name":"sai jaswanth","city":"annavaram"}
>>> a.update({"ph no":9100923316})
>>> a
{'name': 'sai jaswanth', 'city': 'annavaram', 'ph no': 9100923316}
>>> a.update({"f name":"venkataramana","m name":"varalakshmi"})
>>> a
{'name': 'sai jaswanth', 'city': 'annavaram', 'ph no': 9100923316, 'f name': 'venkataramana', 'm name': 'varalakshmi'}
>>> a={"hour":7,"min":23}
>>> a.setdefault("sec":56)
SyntaxError: invalid syntax
>>> a.setdefault("sec",56)
56
>>> a
{'hour': 7, 'min': 23, 'sec': 56}
>>> {'hour': 7, 'min': 23, 'sec': 56}
{'hour': 7, 'min': 23, 'sec': 56}
>>> 
>>> a={"city":"anv","state":"ap","country":"india"}
>>> a.pop("city")
'anv'
>>> a
{'state': 'ap', 'country': 'india'}
>>> a.popitem()
('country', 'india')
>>> ('state','country')
('state', 'country')
>>> a
{'state': 'ap'}
>>> a={"colour":"black","food":"biryani"}
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> b=a.copy()
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> a.clear()
>>> a
{}
len(a)
0
len(b)
2
a={"name"="sai jaswanth","age":18,"name":"sai jaswanth"}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a={"name"="sai","jaswanth","age":18,"name":"sai jaswanth"}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a={"name":"sai jaswanth","age":18,"name":"sai jaswanth"}
a
{'name': 'sai jaswanth', 'age': 18}
b={" name":"ankitha","age":"18","name1":"ankitha"}
b
{' name': 'ankitha', 'age': '18', 'name1': 'ankitha'}
z={"idnos":[10,20,30],"names":["jaswanth","ankitha","sai"]}
print(a)
{'name': 'sai jaswanth', 'age': 18}
type(a)
<class 'dict'>
a.values()
dict_values(['sai jaswanth', 18])
z.values
<built-in method values of dict object at 0x0000020297347EC0>
()
()

z.values()
dict_values([[10, 20, 30], ['jaswanth', 'ankitha', 'sai']])
z.keys()
dict_keys(['idnos', 'names'])
z.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['jaswanth', 'ankitha', 'sai'])])
a=[9,1,5,2,8,4,7,6,3,0]
a.sort()
s
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s
NameError: name 's' is not defined
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.clear()
a
[]
a=[9,1,5,2,8,4,7,6,3,0]
#[7,6,4,3,0,9,8,5,2,1]
a=[9,1,5,2,8,4,7,6,3,0]
a[7:1:1]
[]
a
[9, 1, 5, 2, 8, 4, 7, 6, 3, 0]
a.index(7:1:2)
SyntaxError: invalid syntax
a.index(7)
6

a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=a.copy()
b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
