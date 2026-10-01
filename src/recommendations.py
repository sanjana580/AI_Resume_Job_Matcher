# Learning recommendations and resume improvement suggestions


# -------------------------------------------------
# LEARNING RESOURCES
# -------------------------------------------------

LEARNING_RESOURCES = {

    "data visualization": [
        "Learn Matplotlib",
        "Learn Seaborn",
        "Practice creating charts and dashboards"
    ],

    "deep learning": [
        "Learn neural networks",
        "Study CNNs and RNNs",
        "Build a deep learning project"
    ],

    "natural language processing": [
        "Learn text preprocessing",
        "Study tokenization and embeddings",
        "Build an NLP project"
    ],

    "pytorch": [
        "Learn PyTorch tensors",
        "Learn neural network models",
        "Build a PyTorch classification project"
    ],

    "scikit-learn": [
        "Learn Scikit-learn preprocessing",
        "Practice classification and regression",
        "Learn model evaluation"
    ],

    "statistics": [
        "Learn descriptive statistics",
        "Study probability",
        "Learn hypothesis testing"
    ],

    "tensorflow": [
        "Learn TensorFlow basics",
        "Learn Keras",
        "Build a neural network using TensorFlow"
    ],

    "python": [
        "Practice Python programming",
        "Learn functions and object-oriented programming",
        "Solve Python coding problems"
    ],

    "sql": [
        "Practice SQL queries",
        "Learn JOINs and subqueries",
        "Practice database problems"
    ],

    "machine learning": [
        "Learn supervised learning",
        "Study classification and regression",
        "Practice model evaluation"
    ],

    "pandas": [
        "Practice data manipulation with Pandas",
        "Learn DataFrame operations",
        "Work with real-world datasets"
    ],

    "numpy": [
        "Practice NumPy arrays",
        "Learn numerical operations",
        "Practice matrix operations"
    ],

    "matplotlib": [
        "Learn Matplotlib charts",
        "Practice plotting datasets",
        "Create data visualization projects"
    ]
}


# -------------------------------------------------
# GENERATE LEARNING RECOMMENDATIONS
# -------------------------------------------------

def generate_recommendations(missing_skills):
    """
    Generate learning recommendations
    based on missing skills.
    """

    recommendations = {}

    for skill in missing_skills:

        if skill in LEARNING_RESOURCES:

            recommendations[skill] = (
                LEARNING_RESOURCES[skill]
            )

        else:

            recommendations[skill] = [

                f"Learn the fundamentals of {skill}",

                f"Practice {skill} with a small project",

                f"Build a portfolio project using {skill}"

            ]

    return recommendations


# -------------------------------------------------
# RESUME STRENGTHS
# -------------------------------------------------

def generate_strengths(
    matched_required_skills,
    matched_preferred_skills
):
    """
    Generate resume strengths based on
    matched required and preferred skills.
    """

    strengths = []

    # Required skills are stronger evidence
    # because they are directly requested by
    # the job description.

    for skill in matched_required_skills:

        strengths.append(
            f"Strong match in {skill.title()}"
        )


    # Preferred skills are also useful,
    # but are displayed separately.

    for skill in matched_preferred_skills:

        strengths.append(
            f"Additional experience in {skill.title()}"
        )


    return strengths


# -------------------------------------------------
# IMPROVEMENT SUGGESTIONS
# -------------------------------------------------

def generate_improvement_suggestions(
    missing_required_skills,
    missing_preferred_skills
):
    """
    Generate resume improvement suggestions
    based on missing required and preferred skills.
    """

    suggestions = []


    # Required skills should be prioritized.

    for skill in missing_required_skills:

        suggestions.append(
            f"Consider adding or developing "
            f"{skill.title()} experience."
        )


    # Preferred skills are secondary.

    for skill in missing_preferred_skills:

        suggestions.append(
            f"Consider learning "
            f"{skill.title()} to strengthen your profile."
        )


    return suggestions


# -------------------------------------------------
# TEST
# -------------------------------------------------

if __name__ == "__main__":

    missing_required = [
        "data visualization",
        "scikit-learn",
        "statistics"
    ]

    missing_preferred = [
        "deep learning",
        "pytorch"
    ]

    matched_required = [
        "python",
        "sql",
        "pandas",
        "numpy"
    ]

    matched_preferred = []


    print("Resume Strengths:")

    strengths = generate_strengths(
        matched_required,
        matched_preferred
    )

    for strength in strengths:

        print("-", strength)


    print("\nImprovement Suggestions:")

    suggestions = generate_improvement_suggestions(
        missing_required,
        missing_preferred
    )

    for suggestion in suggestions:

        print("-", suggestion)


    print("\nLearning Recommendations:")

    recommendations = generate_recommendations(
        missing_required + missing_preferred
    )

    for skill, resources in recommendations.items():

        print(f"\n{skill.title()}:")

        for resource in resources:

            print("-", resource)