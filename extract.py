import os
from google import genai
from google.genai import types

def extract_text_from_pdf(pdf_path, prompt):
    try:
        # Create a Gemini client
        client = genai.Client(api_key="YOUR-API-KEY") 

        # Read the PDF file and send it to Gemini model
        with open(pdf_path, 'rb') as file:
            contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_bytes(data=file.read(), mime_type='application/pdf'),
                        types.Part.from_text(text=prompt),
                    ]
                ),
            ]

            # Generate content from Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
                config=types.GenerateContentConfig(
                    response_mime_type="text/plain",
                )
            )

        # Return the extracted text
        return response.text.strip()

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

def save_text_to_file(folder, filename, text):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Save the text to a file in the respective folder
    with open(os.path.join(folder, filename), 'w') as file:
        file.write(text)

def main():
    # Define the paths for input (records) and output (texts, summaries) folders
    records_folder = 'records'
    texts_folder = 'texts'
    summaries_folder = 'summaries'

    # Get the total number of PDFs in the 'records' folder
    total_pdfs = len([f for f in os.listdir(records_folder) if f.endswith('.pdf')])

    # If no PDFs are found, exit early
    if total_pdfs == 0:
        print("No PDF files found in the 'records' folder.")
        return

    # Process each PDF file
    processed_count = 0
    for pdf_filename in os.listdir(records_folder):
        if pdf_filename.endswith('.pdf'):
            text_filename = pdf_filename.replace('.pdf', '.txt')
            summary_filename = pdf_filename.replace('.pdf', '.txt')
            
            text_path = os.path.join(texts_folder, text_filename)
            summary_path = os.path.join(summaries_folder, summary_filename)
            
            # Skip processing if both extracted text and summary already exist
            if os.path.exists(text_path) and os.path.exists(summary_path):
                print(f"Skipping {pdf_filename}, already processed.")
                processed_count += 1
                continue
            
            pdf_path = os.path.join(records_folder, pdf_filename)
            
            # Task 1: Extract text with the first prompt if it doesn't exist
            if not os.path.exists(text_path):
                text_prompt = "Extract only the text from this PDF, without saying anything else"
                extracted_text = extract_text_from_pdf(pdf_path, text_prompt)
                if extracted_text:
                    save_text_to_file(texts_folder, text_filename, extracted_text)
            
            # Task 2: Summarize the document with the second prompt if it doesn't exist
            if not os.path.exists(summary_path):
                summary_prompt = "Summarize this document, without saying anything else"
                summary_text = extract_text_from_pdf(pdf_path, summary_prompt)
                if summary_text:
                    save_text_to_file(summaries_folder, summary_filename, summary_text)
            
            # Increment the processed count and print progress
            processed_count += 1
            print(f"Processed {processed_count}/{total_pdfs} documents")

if __name__ == "__main__":
    main()
