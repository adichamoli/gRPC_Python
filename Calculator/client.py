import sys

import grpc

# import the generated classes
import utility_pb2
import utility_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = utility_pb2_grpc.CalculatorStub(channel)

print ("Please select operation -\n" \
       "1. Add\n" \
       "2. Subtract\n" \
       "3. Multiply\n" \
       "4. Divide\n")

# Take input from the user
select = input ("Select operations form 1, 2, 3, 4 :")

if int(select) > 4:
    print ("Invalid input")
    sys.exit()
input_num1 = int(input("Enter the Number 1 : "))
input_num2 = int(input("Enter the Number 2 : "))

if select == '1':
    response = stub.AddNum(utility_pb2.NumberDouble(value1=input_num1, value2=input_num2))

elif select == '2':
    response = stub.SubNum(utility_pb2.NumberDouble(value1=input_num1, value2=input_num2))

elif select == '3':
    response = stub.MulNum(utility_pb2.NumberDouble(value1=input_num1, value2=input_num2))

elif select == '4':
    response = stub.DivNum(utility_pb2.NumberDouble(value1=input_num1, value2=input_num2))

# et voilà
print(response.value)