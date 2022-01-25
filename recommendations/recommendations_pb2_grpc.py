# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from grpc import Channel, UnaryUnaryMultiCallable, Server, ServicerContext
from grpc._utilities import DictionaryGenericHandler
import recommendations_pb2 as recommendations__pb2
from recommendations_pb2 import RecommendationRequest

class RecommendationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel: Channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend: UnaryUnaryMultiCallable = channel.unary_unary(
                '/Recommendations/Recommend',
                request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.RecommendationResponse.FromString,
                )


class RecommendationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recommend(self, request: RecommendationRequest, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        # TODO remove below
        print("Request variable is of type ", type(request))
        print("Context variable is of type ", type(context))
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationsServicer_to_server(servicer: RecommendationsServicer, server: Server):
    rpc_method_handlers = {
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.RecommendationResponse.SerializeToString,
            ),
    }
    generic_handler: DictionaryGenericHandler = grpc.method_handlers_generic_handler(
            'Recommendations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        # TODO remove below
        print("request variable is of type ", type(request))
        print("target variable is of type ", type(target))
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Recommend',
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.RecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
