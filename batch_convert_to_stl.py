import cadquery as cq
import os
import sys
import shutil

def convert_step_to_stl(input_path, output_path):
    print(f"Converting {input_path} to {output_path}...")
    try:
        # Load the STEP file
        part = cq.importers.importStep(input_path)
        
        # Create a simple assembly and add the part
        # We do NOT apply any rotations here to avoid "exploding" the assembly
        assy = cq.Assembly()
        assy.add(part, name=os.path.basename(input_path))
        
        # Export to STL
        assy.save(output_path, exportType="STL")
        print("Success!")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.step') or file.lower().endswith('.stp'):
                rel_path = os.path.relpath(root, src_dir)
                dest_path_dir = os.path.join(dest_dir, rel_path)
                os.makedirs(dest_path_dir, exist_ok=True)
                
                input_file = os.path.join(root, file)
                output_file = os.path.join(dest_path_dir, os.path.splitext(file)[0] + ".stl")
                
                convert_step_to_stl(input_file, output_file)

if __name__ == "__main__":
    src = "CAD"
    dest = "Configurator/Parts"
    batch_convert(src, dest)
