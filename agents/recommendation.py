from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

def recommendation_agent(request_doc, policy_doc):

    request_lower = request_doc["document_text"].lower()

    # Rule 1 - Back pain > 6 weeks

    pain_duration = any(
        term in request_lower
        for term in [
            "7 weeks",
            "8 weeks",
            "9 weeks",
            "10 weeks",
            "11 weeks",
            "12 weeks",
            "13 weeks",
            "14 weeks",
            "15 weeks",
            "16 weeks",
            "chronic lower back pain"
        ]
    )

    # Rule 2 - Valid Diagnosis

    diagnosis_match = any(
        term in request_lower
        for term in [
            "lumbar radiculopathy",
            "radiculopathy",
            "neurological deficit",
            "suspected disc herniation"
        ]
    )

    # Rule 3 - Treatment Attempted

    treatment_attempted = any(
        term in request_lower
        for term in [
            "physical therapy",
            "medication",
            "medication management",
            "ibuprofen",
            "naproxen"
        ]
    )

    # Decision Logic

    if (
        pain_duration
        and diagnosis_match
        and treatment_attempted
    ):
        return "APPROVE"

    return "DENY"