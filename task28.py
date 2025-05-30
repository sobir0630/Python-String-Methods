commit = 'this is bad'
result = "bad" not in commit.lower().replace("bad", "")
print(result)