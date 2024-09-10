import os

def extract_data():
    input_folder = os.getcwd()
    
    output_img_folder = os.path.join(input_folder, "output_images_dir")
    output_labels_folder = os.path.join(input_folder, "output_labels_dir")
    
    if not os.path.exists(output_img_folder):
        os.makedirs(output_img_folder)
        
    if not os.path.exists(output_labels_folder):
        os.makedirs(output_labels_folder)
        
    for f in os.listdir(output_img_folder):
        if f.endswith(".jpg"):
            image_path = os.path.join(output_img_folder, f)
            print(f"Image found: {image_path}")
            
    for f in os.listdir(output_labels_folder):
        if f.endswith(".jpg"):
            image_path = os.path.join(output_labels_folder, f)
            print(f"label found: {image_path}")

    return output_img_folder, output_labels_folder


output_dir = extract_data()
