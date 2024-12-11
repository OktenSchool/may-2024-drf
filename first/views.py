from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):
    def get(self, *args, **kwargs):
        print(self.request.query_params.dict())
        return Response('hello from get')

    def post(self, *args, **kwargs):
        print(self.request.query_params.dict())

        print(self.request.data)
        return Response('hello from post')

    def put(self, *args, **kwargs):
        return Response('hello from put')

    def patch(self, *args, **kwargs):
        return Response('hello from patch')

    def delete(self, *args, **kwargs):
        return Response('hello from delete')


class SecondView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs['age'])