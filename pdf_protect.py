import PyPDF2
import sys


def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            pdf_writer.encrypt(password)

            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"✅ Password-protected PDF saved as: {output_pdf}")

    except FileNotFoundError:
        print(f"❌ Error: The file {input_pdf} was not found.")
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf, output_pdf, password)


if __name__ == "__main__":
    main()
