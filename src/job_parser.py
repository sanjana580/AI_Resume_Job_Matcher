import re

from src.skill_extractor import extract_skills


def read_job_description(file_path):
    """
    Read a job description from a text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    return job_description


def extract_required_and_preferred_skills(job_text):
    """
    Extract required and preferred skills separately
    from a job description.
    """

    text = job_text.lower()

    required_skills = []
    preferred_skills = []

    # Find Required Skills section
    required_match = re.search(
        r"required skills:(.*?)(?:preferred skills:|$)",
        text,
        re.DOTALL
    )

    # Find Preferred Skills section
    preferred_match = re.search(
        r"preferred skills:(.*)",
        text,
        re.DOTALL
    )

    if required_match:
        required_text = required_match.group(1)
        required_skills = extract_skills(required_text)

    if preferred_match:
        preferred_text = preferred_match.group(1)
        preferred_skills = extract_skills(preferred_text)

    return required_skills, preferred_skills


if __name__ == "__main__":

    job_path = "data/job_descriptions/data_scientist.txt"

    job_text = read_job_description(job_path)

    required_skills, preferred_skills = (
        extract_required_and_preferred_skills(
            job_text
        )
    )

    print("Required Skills:")

    for skill in required_skills:
        print("-", skill)

    print("\nPreferred Skills:")

    for skill in preferred_skills:
        print("-", skill)