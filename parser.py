from pathlib import Path

def get_input(file_name, split=None):
  project_root = Path(__file__).parent
  input_path = project_root / "inputs" / file_name
  with open(input_path, "r") as f:
    content = f.read()
  if split is None:
    return content
  else:
    return content.split(split)
