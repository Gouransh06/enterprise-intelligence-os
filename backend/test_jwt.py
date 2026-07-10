from app.auth.jwt import create_access_token, verify_access_token

token = create_access_token(
    {
        "sub": "gouransh"
    }
)

print("TOKEN")
print(token)

print()

payload = verify_access_token(token)

print("PAYLOAD")
print(payload)