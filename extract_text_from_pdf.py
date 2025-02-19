def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)  # Create a PDF reader object
    extracted_pages = []  # Initialize a list to store extracted text along with page numbers                       
    for page_num, page in enumerate(reader.pages):  # Iterate through each page in the PDF
        text = page.extract_text() or ""  # Extract text from the page; default to empty string if None
        extracted_pages.append((text.strip(), page_num + 1))  # Store text (stripped of leading/trailing spaces) and page number
    return extracted_pages  # Return a list of tuples containing text and corresponding page numbers

def chunk_text(text, chunk_size=1000, overlap=200): # Split the input text into chunks of a specified size with optional overlap between consecutive chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)  # Create a splitter instance with the specified chunk size and overlap
    return splitter.split_text(text)  # Use the splitter to divide the text into chunks and return the result  
