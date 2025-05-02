import os
from PyPDF2 import PdfReader, PdfWriter

def unlock_pdf(input_pdf_path, output_pdf_path, password):
    try:
        # Read the encrypted PDF
        with open(input_pdf_path, 'rb') as file:
            reader = PdfReader(file)
            
            # Try to decrypt using the password
            if reader.decrypt(password):
                writer = PdfWriter()
                
                # Add all pages to the writer
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])
                
                # Write the unlocked PDF to a new file
                with open(output_pdf_path, 'wb') as output_file:
                    writer.write(output_file)
                
                print(f"✅ PDF unlocked successfully! Saved as: {output_pdf_path}")
            else:
                print("❌ Incorrect password.")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# Main Program
folder_path = input("Enter the full path of the folder containing PDF files: ").strip('"')

if not os.path.isdir(folder_path):
    print("❌ Invalid folder path.")
    exit()

input_pdf = input("Enter the name of the password-protected PDF file: ").strip('"')
password = input("Enter the password for the PDF file: ").strip('"')

input_pdf_path = os.path.join(folder_path, input_pdf)
output_pdf_path = os.path.join(folder_path, f"unlocked_{input_pdf}")

if not os.path.exists(input_pdf_path):
    print(f"❌ The file {input_pdf} does not exist in the specified folder.")
else:
    unlock_pdf(input_pdf_path, output_pdf_path, password)
