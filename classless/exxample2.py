config_data = {}

def set_config(key, value):
    config_data[key] = value

def get_config(key):
    return config_data.get(key)

# Example usage
set_config('username', 'user123')
set_config('password', 'pass456')

username = get_config('username')
password = get_config('password')

print("Username:", username)
print("Password:", password)