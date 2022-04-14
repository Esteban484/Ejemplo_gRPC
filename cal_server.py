from concurrent import futures
import grpc
import SimpleCal_pb2
import SimpleCal_pb2_grpc
 
class CalServicer(SimpleCal_pb2_grpc.CalServicer):
 Def Add (self, request, context): #Agregar lógica de implementación
    print("Add function called")
    return SimpleCal_pb2.ResultReply(number=request.number1 + request.number2)
 
 Def Multiply (self, request, context): # # Lógica de implementación de la función Multiply
    print("Multiply service called")
    return SimpleCal_pb2.ResultReply(number=request.number1 * request.number2)
 
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
  SimpleCal_pb2_grpc.add_CalServicer_to_server(CalServicer(),server)
  server.add_insecure_port("[::]:50051")
  server.start()
  print("grpc server start...")
  server.wait_for_termination()
 
if __name__ == '__main__':
  serve()