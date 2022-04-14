from multiprocessing.sharedctypes import Value
import grpc

# Importacion de clases generadas
import calculator_pb2
import calculator_pb2_grpc

# Abriendo el canal gRPC
channel = grpc.insecure_channel('localhost:50051')

# Creacion del stub (cliente)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# creaando un mensaje de solictud valido
number = calculator_pb2.Number(value=25)

# Se hace la llamada
response = stub.SquareRoot(number)

# Respuesta del servidor
print(response.value)