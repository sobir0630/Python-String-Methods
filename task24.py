user = 'user@example.com'
result = not user.startswith('@') and user.endswith('.com')
print(result)