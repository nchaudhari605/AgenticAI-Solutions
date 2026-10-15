# def validation_agent(document):

#     missing = []

#     if "NOT PROVIDED" in document:

#         missing.append(
#             "Physical Therapy History"
#         )

#     return missing

def validation_agent(data):

    missing = []

    if not data["contains_diagnosis"]:
        missing.append("Diagnosis")

    if not data["contains_provider_notes"]:
        missing.append("Provider Notes")

    if not data["contains_treatment_history"]:
        missing.append("Treatment History")

    return missing