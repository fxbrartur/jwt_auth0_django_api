import jwt


key = "TAuKMlDq9bEqoenSM7W2x"
encoded = jwt.encode({
  "iss": "https://dev-352za0lu0zfx5z5w.us.auth0.com/",
  "sub": "uAuZlnLhKLunye1xaGV6rxVz3hes1QNX@clients",
  "aud": "https://assessment/api",
  "iat": 1670898570,
  "exp": 1670984970,
  "azp": "uAuZlnLhKLunye1xaGV6rxVz3hes1QNX",
  "scope": "read:messages",
  "gty": "client-credentials",
  "cpf": "80692578650",
  "name": "123 de Oliveira 4",
}, key, algorithm="HS256")

print(encoded)

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2Rldi0zNTJ6YTBsdTB6Zng1ejV3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWEBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hc3Nlc3NtZW50L2FwaSIsImlhdCI6MTY3MDg5ODU3MCwiZXhwIjoxNjcwOTg0OTcwLCJhenAiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWCIsInNjb3BlIjoicmVhZDptZXNzYWdlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImNwZiI6IjA4NjkyODc0NDUwIiwibmFtZSI6IjEyMyBkZSBPbGl2ZWlyYSA0In0.7nlhk2uw5WbDtrH6LzopmVqYoUHEuDy8B0zeOVFkpys
  # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2Rldi0zNTJ6YTBsdTB6Zng1ejV3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWEBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hc3Nlc3NtZW50L2FwaSIsImlhdCI6MTY3MDg5ODU3MCwiZXhwIjoxNjcwOTg0OTcwLCJhenAiOiJ1QXVabG5MaEtMdW55ZTF4YUdWNnJ4VnozaGVzMVFOWCIsInNjb3BlIjoicmVhZDptZXNzYWdlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImNwZl9kaXNwb25pdmVsIjoidHJ1ZSIsIm5hbWUiOiJmYWxzZSIsIm5hbWVfc2ltaWxhcml0eSI6IjAuMzgwOTUyMzgwOTUyMzgwOTMiLCJzaXR1YWNhb19jcGYiOiJ0cnVlIn0.cJfNTAH3PoUOKxw_rgXl8rNgofRHUVpiu2WTwPPcCK0