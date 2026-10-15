def intake_agent(data):

    print("✅ Intake Agent Running")

    # JSON Request
    if isinstance(data, dict):

        extracted_data = {
            "document_text": str(data),

            "contains_diagnosis":
                bool(data.get("diagnosis")),

            "contains_provider_notes":
                bool(data.get("provider_notes")),

            "contains_treatment_history":
                bool(data.get("treatment_history"))
        }

    # TXT / PDF / CSV text
    else:

        document = str(data).lower()

        extracted_data = {
            "document_text": str(data),

            "contains_diagnosis":
                "diagnosis" in document,

            "contains_provider_notes":
                (
                    "provider notes" in document
                    or "provider_notes" in document
                ),

            "contains_treatment_history":
                (
                    "treatment history" in document
                    or "treatment_history" in document
                )
        }

    return extracted_data