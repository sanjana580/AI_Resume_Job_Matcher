from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.units import inch


def format_skill_name(skill):

    skill_names = {

        "python": "Python",
        "java": "Java",
        "c": "C",
        "sql": "SQL",
        "mysql": "MySQL",

        "pandas": "Pandas",
        "numpy": "NumPy",
        "matplotlib": "Matplotlib",

        "scikit-learn": "Scikit-learn",

        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",

        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",

        "natural language processing":
            "Natural Language Processing",

        "computer vision":
            "Computer Vision",

        "statistics":
            "Statistics",

        "data preprocessing":
            "Data Preprocessing",

        "data visualization":
            "Data Visualization",

        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript",

        "git": "Git",
        "github": "GitHub",

        "fastapi": "FastAPI",
        "streamlit": "Streamlit"
    }

    return skill_names.get(
        skill.lower(),
        skill.title()
    )


def generate_pdf_report(
    output_path,
    resume_name,
    required_match,
    semantic_score,
    preferred_match,
    final_score,
    matched_required_skills,
    missing_required_skills,
    matched_preferred_skills,
    missing_preferred_skills,
    strengths,
    improvement_suggestions,
    recommendations,
    interview_questions
):

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=15,
        spaceBefore=12,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=5
    )

    small_style = ParagraphStyle(
        "SmallStyle",
        parent=styles["BodyText"],
        fontSize=9,
        leading=12
    )

    story = []

    # -------------------------------------------------
    # TITLE
    # -------------------------------------------------

    story.append(
        Paragraph(
            "AI Resume Job Matcher",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Resume:</b> {resume_name}",
            normal_style
        )
    )

    story.append(Spacer(1, 10))

    # -------------------------------------------------
    # SCORE SUMMARY
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Match Results",
            heading_style
        )
    )

    score_data = [
        ["Metric", "Score"],
        [
            "Required Skills Match",
            f"{required_match:.2f}%"
        ],
        [
            "Semantic Match",
            f"{semantic_score:.2f}%"
        ],
        [
            "Preferred Skills Match",
            f"{preferred_match:.2f}%"
        ],
        [
            "Final AI Score",
            f"{final_score:.2f}%"
        ]
    ]

    score_table = Table(
        score_data,
        colWidths=[3.8 * inch, 1.8 * inch]
    )

    score_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.black
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "FONTNAME",
                (0, -1),
                (-1, -1),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (1, -1),
                "CENTER"
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                7
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                7
            )
        ])
    )

    story.append(score_table)

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # AI ANALYSIS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "AI Analysis Summary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"Your resume matches "
            f"<b>{required_match:.0f}%</b> of the required "
            f"skills for this role.",
            normal_style
        )
    )

    if matched_required_skills:

        skills = ", ".join(
            format_skill_name(skill)
            for skill in matched_required_skills
        )

        story.append(
            Paragraph(
                f"<b>Strongest technical matches:</b> "
                f"{skills}.",
                normal_style
            )
        )

    if missing_required_skills:

        skills = ", ".join(
            format_skill_name(skill)
            for skill in missing_required_skills
        )

        story.append(
            Paragraph(
                f"<b>Main required skill gaps:</b> "
                f"{skills}.",
                normal_style
            )
        )

    if missing_preferred_skills:

        skills = ", ".join(
            format_skill_name(skill)
            for skill in missing_preferred_skills
        )

        story.append(
            Paragraph(
                f"<b>Additional preferred skills:</b> "
                f"{skills}.",
                normal_style
            )
        )

    # -------------------------------------------------
    # STRENGTHS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Resume Strengths",
            heading_style
        )
    )

    if strengths:

        for strength in strengths:

            story.append(
                Paragraph(
                    f"• {strength}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "No specific strengths detected.",
                normal_style
            )
        )

    # -------------------------------------------------
    # IMPROVEMENT SUGGESTIONS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Improvement Suggestions",
            heading_style
        )
    )

    if improvement_suggestions:

        for suggestion in improvement_suggestions:

            story.append(
                Paragraph(
                    f"• {suggestion}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "No major improvement suggestions.",
                normal_style
            )
        )

    # -------------------------------------------------
    # REQUIRED SKILLS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Required Skills",
            heading_style
        )
    )

    if matched_required_skills:

        story.append(
            Paragraph(
                "<b>Matched:</b>",
                normal_style
            )
        )

        for skill in matched_required_skills:

            story.append(
                Paragraph(
                    f"• {format_skill_name(skill)}",
                    normal_style
                )
            )

    if missing_required_skills:

        story.append(
            Paragraph(
                "<b>Missing:</b>",
                normal_style
            )
        )

        for skill in missing_required_skills:

            story.append(
                Paragraph(
                    f"• {format_skill_name(skill)}",
                    normal_style
                )
            )

    # -------------------------------------------------
    # PREFERRED SKILLS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Preferred Skills",
            heading_style
        )
    )

    if matched_preferred_skills:

        story.append(
            Paragraph(
                "<b>Matched:</b>",
                normal_style
            )
        )

        for skill in matched_preferred_skills:

            story.append(
                Paragraph(
                    f"• {format_skill_name(skill)}",
                    normal_style
                )
            )

    if missing_preferred_skills:

        story.append(
            Paragraph(
                "<b>Missing:</b>",
                normal_style
            )
        )

        for skill in missing_preferred_skills:

            story.append(
                Paragraph(
                    f"• {format_skill_name(skill)}",
                    normal_style
                )
            )

    # -------------------------------------------------
    # LEARNING RECOMMENDATIONS
    # -------------------------------------------------

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Learning Recommendations",
            heading_style
        )
    )

    if recommendations:

        for skill, resources in recommendations.items():

            story.append(
                Paragraph(
                    format_skill_name(skill),
                    ParagraphStyle(
                        "SkillHeading",
                        parent=normal_style,
                        fontName="Helvetica-Bold",
                        fontSize=11
                    )
                )
            )

            for resource in resources:

                story.append(
                    Paragraph(
                        f"• {resource}",
                        normal_style
                    )
                )

    # -------------------------------------------------
    # INTERVIEW QUESTIONS
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Interview Questions",
            heading_style
        )
    )

    if interview_questions:

        for skill, questions in interview_questions.items():

            story.append(
                Paragraph(
                    format_skill_name(skill),
                    ParagraphStyle(
                        "QuestionSkill",
                        parent=normal_style,
                        fontName="Helvetica-Bold",
                        fontSize=11
                    )
                )
            )

            for question in questions:

                story.append(
                    Paragraph(
                        f"• {question}",
                        normal_style
                    )
                )

    # -------------------------------------------------
    # FOOTER
    # -------------------------------------------------

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by AI Resume Job Matcher",
            small_style
        )
    )

    # -------------------------------------------------
    # BUILD PDF
    # -------------------------------------------------

    document.build(story)