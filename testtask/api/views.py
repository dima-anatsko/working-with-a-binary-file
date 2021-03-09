from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .binary import get_keys, create_data, put_value, delete_data, \
    find_data, get_key_value
from .permissions import IsAdminOrReadOnly
from .serializers import LoginSerializer, SignUpSerializer


class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer


class SignUpApiView(CreateAPIView):
    serializer_class = SignUpSerializer


class FileView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            keys = get_keys()
        else:
            keys = find_data(query)
        return Response({"keys": keys}, status=200)

    def post(self, request):
        try:
            key, value = get_key_value(request)
        except TypeError as e:
            return Response({"errors": e.args}, status=400)
        create_data(key, value)
        return Response({"success": "Data created successfully"}, status=201)

    def put(self, request):
        try:
            key, value = get_key_value(request)
        except TypeError as e:
            return Response({"errors": e.args}, status=400)
        try:
            put_value(key, value)
        except KeyError as e:
            return Response(e.args)
        return Response(
            {"success": f"Value with key={key} updated successfully"},
            status=201)

    def delete(self, request):
        data = request.data.get('data')
        key = data.get('key')
        try:
            delete_data(key)
        except KeyError as e:
            return Response(e.args)
        return Response({
            "message": f"Data with key=`{key}` has been deleted."}, status=204)
