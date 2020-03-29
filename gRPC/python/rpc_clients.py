# Created at 2020. 3. 1.

__author__ = "hyeockkwon"

# from __future__ import print_function
import logging

import grpc

import practice_pb2
import practice_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = practice_pb2_grpc.ChannelRPCStub(channel)
        response = stub.TestConn(practice_pb2.ConnRequest(status_text='Success'))

        print("TestConn status: {} / message: {}".format(response.status, response.message))


if __name__ == '__main__':
    logging.basicConfig()
    run()
