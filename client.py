import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

input_num = int(input("Enter the Number : "))
# create a valid request message
number = calculator_pb2.Number(value=input_num)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)