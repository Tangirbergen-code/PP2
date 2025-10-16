def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.title() for word in parts[1:])

print(snake_to_camel('hello_world_example'))
