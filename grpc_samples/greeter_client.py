# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        response2 = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='person'))
        try:
            send = input('Enter the name of the sender: ')
            receive = input('Enter the name of the receiver: ')
            amount = int(input('Enter amount: '))
        except:
            send = 'Person A'
            receive = 'Person B'
            amount = 100
        stubInfo = helloworld_pb2_grpc.InfoStub(channel)
        response3 = stubInfo.DisplayInfo(helloworld_pb2.InfoRequest(Sender=send,Receiver=receive,Amount=amount))

    print('Greeter client received: ' + response.message)
    print('Greeter client received: ' + response2.message)
    print('Received: ' + response3.message)


if __name__ == '__main__':
    run()
