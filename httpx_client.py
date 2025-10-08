import time
import httpx

# Инициализируем клиент
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=60
)

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем POST-запрос, используя клиент
response = client.post("/api/v1/users", json=payload)

# Выводим ответ в консоль
print(response.text)
