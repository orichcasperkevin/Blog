from contextlib import contextmanager

# Global configuration dictionary
global_config = {'debug_mode': False, 'timeout': 10}

@contextmanager
def temporary_config_change(new_value, key):
    # Save the original value
    original_value = global_config[key]
    # Change the global configuration value temporarily
    global_config[key] = new_value

    yield

    #reset config.
    global_config[key] = original_value


# Example usage
print("Original Configuration:", global_config)
with temporary_config_change(True, 'debug_mode'):
    print("Configuration Inside Context:", global_config)
    # Some code that runs with the modified configuration


print("Configuration After Context:", global_config)
