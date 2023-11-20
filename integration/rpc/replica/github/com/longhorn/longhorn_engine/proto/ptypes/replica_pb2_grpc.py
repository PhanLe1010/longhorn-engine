# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.longhorn.longhorn_engine.proto.ptypes import replica_pb2 as github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ReplicaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReplicaCreate = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaCreate',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateResponse.FromString,
                )
        self.ReplicaDelete = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaDelete',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReplicaGet = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaGet',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaGetResponse.FromString,
                )
        self.ReplicaOpen = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaOpen',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaOpenResponse.FromString,
                )
        self.ReplicaClose = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaClose',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCloseResponse.FromString,
                )
        self.ReplicaReload = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaReload',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaReloadResponse.FromString,
                )
        self.ReplicaRevert = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaRevert',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertResponse.FromString,
                )
        self.ReplicaSnapshot = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaSnapshot',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotResponse.FromString,
                )
        self.ReplicaExpand = channel.unary_unary(
                '/ptypes.ReplicaService/ReplicaExpand',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandResponse.FromString,
                )
        self.DiskRemove = channel.unary_unary(
                '/ptypes.ReplicaService/DiskRemove',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveResponse.FromString,
                )
        self.DiskReplace = channel.unary_unary(
                '/ptypes.ReplicaService/DiskReplace',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceResponse.FromString,
                )
        self.DiskPrepareRemove = channel.unary_unary(
                '/ptypes.ReplicaService/DiskPrepareRemove',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveResponse.FromString,
                )
        self.DiskMarkAsRemoved = channel.unary_unary(
                '/ptypes.ReplicaService/DiskMarkAsRemoved',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedResponse.FromString,
                )
        self.RebuildingSet = channel.unary_unary(
                '/ptypes.ReplicaService/RebuildingSet',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetResponse.FromString,
                )
        self.RevisionCounterSet = channel.unary_unary(
                '/ptypes.ReplicaService/RevisionCounterSet',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetResponse.FromString,
                )
        self.UnmapMarkDiskChainRemovedSet = channel.unary_unary(
                '/ptypes.ReplicaService/UnmapMarkDiskChainRemovedSet',
                request_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.FromString,
                )


class ReplicaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReplicaCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaOpen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaClose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaReload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaRevert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaExpand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskReplace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskPrepareRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskMarkAsRemoved(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RebuildingSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevisionCounterSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnmapMarkDiskChainRemovedSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplicaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReplicaCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaCreate,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateResponse.SerializeToString,
            ),
            'ReplicaDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaDelete,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReplicaGet': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaGet,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaGetResponse.SerializeToString,
            ),
            'ReplicaOpen': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaOpen,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaOpenResponse.SerializeToString,
            ),
            'ReplicaClose': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaClose,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCloseResponse.SerializeToString,
            ),
            'ReplicaReload': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaReload,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaReloadResponse.SerializeToString,
            ),
            'ReplicaRevert': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaRevert,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertResponse.SerializeToString,
            ),
            'ReplicaSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaSnapshot,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotResponse.SerializeToString,
            ),
            'ReplicaExpand': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaExpand,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandResponse.SerializeToString,
            ),
            'DiskRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskRemove,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveResponse.SerializeToString,
            ),
            'DiskReplace': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskReplace,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceResponse.SerializeToString,
            ),
            'DiskPrepareRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskPrepareRemove,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveResponse.SerializeToString,
            ),
            'DiskMarkAsRemoved': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskMarkAsRemoved,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedResponse.SerializeToString,
            ),
            'RebuildingSet': grpc.unary_unary_rpc_method_handler(
                    servicer.RebuildingSet,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetResponse.SerializeToString,
            ),
            'RevisionCounterSet': grpc.unary_unary_rpc_method_handler(
                    servicer.RevisionCounterSet,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetResponse.SerializeToString,
            ),
            'UnmapMarkDiskChainRemovedSet': grpc.unary_unary_rpc_method_handler(
                    servicer.UnmapMarkDiskChainRemovedSet,
                    request_deserializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.FromString,
                    response_serializer=github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ptypes.ReplicaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReplicaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReplicaCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaCreate',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaDelete',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaGet',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaOpen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaOpen',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaOpenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaClose',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaReload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaReload',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaReloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaRevert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaRevert',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaRevertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaSnapshot',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaExpand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/ReplicaExpand',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.ReplicaExpandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/DiskRemove',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskRemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskReplace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/DiskReplace',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskReplaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskPrepareRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/DiskPrepareRemove',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskPrepareRemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskMarkAsRemoved(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/DiskMarkAsRemoved',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.DiskMarkAsRemovedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RebuildingSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/RebuildingSet',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RebuildingSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevisionCounterSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/RevisionCounterSet',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.RevisionCounterSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnmapMarkDiskChainRemovedSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.ReplicaService/UnmapMarkDiskChainRemovedSet',
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.SerializeToString,
            github_dot_com_dot_longhorn_dot_longhorn__engine_dot_proto_dot_ptypes_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
