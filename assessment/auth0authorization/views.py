from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from functools import wraps
import jwt


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'Datavalid': 'OK - O servico Datavalid esta operando normalmente'})

@api_view(['POST'])
def consulta(request):
    return JsonResponse({'message': 'SERPRO RESPONSE WOULD BE HERE'})

@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})

@api_view(['POST'])
def receive_jwt(request):
    # Get the JWT from the request
    jwt = request.data.get('jwt')

    # Validate the JWT
    if not jwt:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Missing JWT'})

    # TODO: validate the JWT, check if it is valid and not expired, etc.

    # Return a new JWT
    return Response(data={'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2Rldi0zNTJ6YTBsdTB6Zng1ejV3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWEBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hc3Nlc3NtZW50L2FwaSIsImlhdCI6MTY3MDg5ODU3MCwiZXhwIjoxNjcwOTg0OTcwLCJhenAiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWCIsInNjb3BlIjoicmVhZDptZXNzYWdlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImNwZl9kaXNwb25pdmVsIjoidHJ1ZSIsIm5hbWUiOiJmYWxzZSIsIm5hbWVfc2ltaWxhcml0eSI6IjAuMzgwOTUyMzgwOTUyMzgwOTMiLCJzaXR1YWNhb19jcGYiOiJ0cnVlIn0.cJfNTAH3PoUOKxw_rgXl8rNgofRHUVpiu2WTwPPcCK0'})
