input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
b = 1
s = int(((b + a)/2)*a)
output_data = open("output.txt","w")
output_data.write(str(s))
input_data.close()
output_data.close()
"""
for i in range(1,a,1):
    print(i)
    if i == 55:
        break
    print(i)
"""



