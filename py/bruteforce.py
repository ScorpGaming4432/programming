import itertools

def brute_force(target, character_set, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(character_set, repeat=length):
            brute_force_attempt = ''.join(attempt)
            if brute_force_attempt == target:
                return brute_force_attempt
    return None

target_password = "abc"
charset = "abcdefghijklmnopqrstuvwxyz"
max_length = 3

result = brute_force(target_password, charset, max_length)
if result:
    print(f"Hasło znalezione: {result}")
else:
    print("Nie udało się znaleźć hasła.")