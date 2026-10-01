def calculate_match(resume_skills, job_skills):
    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    if not job_skills:
        return 0

    matched_skills = resume_skills.intersection(job_skills)

    match_percentage = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(match_percentage, 2)


def find_missing_skills(resume_skills, job_skills):
    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    missing_skills = job_skills - resume_skills

    return sorted(missing_skills)


def calculate_weighted_score(
    required_match,
    semantic_score,
    preferred_match
):
    final_score = (
        (required_match * 0.60)
        + (semantic_score * 0.30)
        + (preferred_match * 0.10)
    )

    return round(float(final_score), 2)