input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
sum = 0
for i in range(1,a + 1):
    sum = sum + i
output_data = open("output.txt","w")
output_data.write(str(sum))
output_data.close()
input_data.close()
    



