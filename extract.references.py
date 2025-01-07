import sys
from refextract import extract_references_from_file

from refextract import extract_references_from_file

def extract_references(pdf_path, output_path):
    # Extract references from the PDF file
    references = extract_references_from_file(pdf_path)

    # Write the extracted references to a plain text file
    with open(output_path, 'w') as f:
        for ref in references:
            # Ensure raw_ref is a string
            if isinstance(ref['raw_ref'], list):
                ref_text = ' '.join(ref['raw_ref'])
            else:
                ref_text = ref['raw_ref']
            f.write(ref_text + '\n\n')  # Write each reference on a new line


if __name__ == "__main__":
    pdf_path = sys.argv[1] # 'example.pdf'  # Path to your PDF file
    output_path = 'references.txt'  # Output plain text file

    extract_references(pdf_path, output_path)

    print(f'References extracted and saved to {output_path}')

