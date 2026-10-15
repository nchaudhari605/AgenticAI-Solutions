def communication_agent(request_doc, recommendation):

    email = "Not Provided"
    patient_name = "Member"

    for line in request_doc.split("\n"):

        if "Patient Name:" in line:
            patient_name = line.split(":", 1)[1].strip()

        if "Provider Email:" in line:
            email = line.split(":", 1)[1].strip()

    if "APPROVE" in recommendation:

        return f"""
Subject: Prior Authorization Approved

Dear {patient_name},

Your prior authorization request has been approved.

Please coordinate with your provider regarding next steps.

Thank you,
Health Plan Prior Authorization Team

Email Contact: {email}
"""

    return f"""
Subject: Additional Information Required

Dear Provider,

Additional documentation is required before a decision can be made.

Please submit the requested information.

Contact Email: {email}
"""