from rembg import remove;
import sys;

def set_output_path(input_path):
	filename_without_format = input_path.split("/")[-1].split(".")[0]
	output_filename = filename_without_format + ".png"
	return "/".join(input_path.split("/")[:-1]) + f"/{output_filename}"

def rembg_main(input_path = ""):
  if len(input_path) == 0:
    print("Input path not specified")
    return
  output_path = set_output_path(input_path)
  try:
  	with open(input_path, 'rb') as i:
  		with open(output_path, 'wb') as o:
  			print(f"Processing: {input_path}")
  			input = i.read()
  			output = remove(input, post_process_mask=True)
  			o.write(output)
  			print(f"\nImage output location: {output_path}")
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
