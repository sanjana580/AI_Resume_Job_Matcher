import pymupdf


def extract_resume_text(pdf_path):
    """
    Extract text from a resume PDF.
    """

    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


if __name__ == "__main__":
    resume_path = "data/resumes/sanjana.pdf"

    resume_text = extract_resume_text(resume_path)

    print(resume_text)