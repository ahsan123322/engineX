from enginex import process_pdf, crawl_and_query,config

# Example 1: Processing a PDF
pdf_path = "Chap.pdf"
pdf_query = "Formal Document?"

pdf_results = process_pdf(pdf_path, pdf_query)

print("PDF Results:")
for chunk, similarity in pdf_results:
    print(f"Similarity: {similarity:.4f}")
    print(f"Chunk: {chunk[:200]}...")  # Print first 200 characters
    print("-" * 50)

