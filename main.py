from rembg import remove
import sys
import os

def path_separator() -> str:
  return "\\" if os.name == "nt" else "/"

def set_output_path(input_path) -> str:
  filename_without_format = input_path.split(path_separator())[-1].split(".")[0]
  output_filename = path_separator() + filename_without_format + ".png"
  output_path = ""
  if os.name != "nt":
    output_path += "/"
  return output_path + (path_separator()).join(input_path.split(path_separator())[:-1]) + output_filename

def rembg_main(input_path = ""):
  if len(input_path) == 0:
    print("Input path not specified")
    return
  input_path = input_path.replace("/" if os.name == "nt" else "\\", "\\" if os.name == "nt" else "/")
  output_path = set_output_path(input_path)
  try:
    with open(input_path, 'rb') as i:
      try:
        with open(output_path, 'wb') as o:
          print(f"Processing: {input_path}")
          input = i.read()
          output = remove(input, post_process_mask=True)
          o.write(output)
          print(f"\nImage output location: {output_path}")
          return
      except:
        print("Error: Output path maybe invalid")
        return
  except FileNotFoundError:
    print(f"Error: Input file not exist")
    return

if __name__ == "__main__":
  args = sys.argv[1:]
  try:
    if len(args) > 1:
      print("Error: Invalid argument")
      exit(2)
    rembg_main(args[0])
  except IndexError:
    if len(args) == 0:
      print("Error: Input image not specified")
