import grpc
from concurrent import futures
import time

# import the generated classes
import utility_pb2
import utility_pb2_grpc

# import the original utility.py
import utility

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(utility_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def AddNum(self, request, context):
        response = utility_pb2.Number()
        response.value = utility.add_num(request.value1, request.value2)
        return response

    def SubNum(self, request, context):
        response = utility_pb2.Number()
        response.value = utility.sub_num(request.value1, request.value2)
        return response

    def MulNum(self, request, context):
        response = utility_pb2.Number()
        response.value = utility.mul_num(request.value1, request.value2)
        return response

    def DivNum(self, request, context):
        response = utility_pb2.Number()
        response.value = utility.div_num(request.value1, request.value2)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
utility_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)