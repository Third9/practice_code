# Created at 2020. 3. 1.

__author__ = "hyeockkwon"

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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import practice_pb2
import practice_pb2_grpc


class ChannelRPC(practice_pb2_grpc.ChannelRPCServicer):

    def TestConn(self, request, context):
        return practice_pb2.ConnResponse(status=200, message="Connect {}".format(request.status_text))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    practice_pb2_grpc.add_ChannelRPCServicer_to_server(ChannelRPC(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
