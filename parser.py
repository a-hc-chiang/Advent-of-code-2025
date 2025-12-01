def get_input(file_name):
  with open(f'inputs/{file_name}', 'r') as f:
    return f.read().split('\n')