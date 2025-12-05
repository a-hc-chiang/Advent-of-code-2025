from pathlib import Path

def get_input(file_name, split):
  project_root = Path(__file__).parent
  input_path = project_root / 'inputs' / file_name
  
  with open(input_path, 'r') as f:
    return f.read().split(split)
