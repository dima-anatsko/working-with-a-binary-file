from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import get_keys, post_data, validated_data, put_value, \
    delete_data


class FileView(APIView):
    def get(self, request):
        keys = get_keys()
        return Response({"keys": keys}, status=200)

    def post(self, request):
        data = request.data.get('data')
        key = data.get('key')
        value = data.get('value')
        if not validated_data(key, value):
            return Response({"error": "Bad key or value"}, status=400)
        post_data(key, value)
        return Response({"success": "Data created successfully"}, status=201)

    def put(self, request, key):
        data = request.data.get('data')
        value = data.get('value')
        if not validated_data(key, value):
            return Response({"error": "Bad key or value"}, status=400)
        try:
            put_value(key, value)
        except KeyError as e:
            return Response(e.args)
        return Response(
            {"success": f"Value with key={key} updated successfully"},
            status=201)

    def delete(self, request, key):
        try:
            delete_data(key)
        except KeyError as e:
            return Response(e.args)
        return Response({
            "message": f"Data with key=`{key}` has been deleted."}, status=204)
