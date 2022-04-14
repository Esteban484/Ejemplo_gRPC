import grpc
from concurrent import futures
import time

# Importacion de clases
import calculator_pb2
import calculator_pb2_grpc

# importacion del calculator original calculator.py
import calculator

# Creacion de clases para define las funciones del servidor provenientes de
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # se calcula la raiz cuadrarda del numeor enviado por el cliente
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


# creacion de gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#Usar el servicio de claculadora para el servidor
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# Escucahdno desde el puerto 50051
print('Servidor levantado. escuchando por el puerto 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# Ya que el servidor no se bloqueara se añade un sleep para que siga funcionando
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)