# Raw to JPEG Bulk Converter

As a photographer who uses RAW files, I know firsthand that professional photos can take up a massive amount of space – sometimes more than **10GB** right after a trip! To save space while keeping my holiday photos, I developed this program. It converts **RAW photos to smaller, more space-friendly JPEGs**!

This way, you can **keep your best photos in PNG/RAW** and convert the rest to JPEGs. It's very easy to use! 😊

## 🚀 Features

- **RAW to JPEG Conversion**  
  Converts popular RAW file formats (e.g., `.nef`, `.cr2`, `.cr3`, `.arw`, `.dng`) into JPEG format.

- **Adjustable JPEG Quality**  
  Allows you to specify the desired JPEG quality percentage (from **1 to 100**) for an optimal balance between image quality and file size.

- **Recursive Directory Traversal**  
  Processes all images in the specified folder and its subdirectories while maintaining the original folder structure in the output.

- **Non-RAW File Handling**  
  Automatically **copies non-RAW files** to the output directory to preserve the complete file hierarchy.

## 🛠️ How to Run

Simply execute the script from the command line by providing the **path to the folder** containing your images and the **desired JPEG quality percentage**. For example:

```bash
./advanced_image_converter.py /path/to/images 85
