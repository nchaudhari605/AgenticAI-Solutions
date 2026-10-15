import streamlit as st
import pandas as pd
import json

from agents.intake import intake_agent
from agents.validation import validation_agent
from agents.policy import policy_agent
from agents.recommendation import recommendation_agent

st.title("AI Prior Authorization Master File Processing")

uploaded_file = st.file_uploader(
    "Upload Master JSON File",
    type=["json"]
)

if uploaded_file:

    requests = json.load(uploaded_file)

    if st.button("Process All Members"):

        approved = 0
        pending = 0
        denied = 0

        results = []

        policy = policy_agent()

        for request in requests:

            intake_result = intake_agent(request)

            missing = validation_agent(
                intake_result
            )

            # Step 1: Missing docs = PEND
            if missing:

                status = "PEND"
                pending += 1

                reason = "Required documentation is missing"
                next_action = "Provider Outreach"

            else:

                recommendation = recommendation_agent(
                    intake_result,
                    policy
                )

                # Step 2: Criteria met?
                if "APPROVE" in recommendation:

                    status = "APPROVE"
                    approved += 1

                    reason = "All policy criteria met"
                    next_action = "Ready For Human Review"

                else:

                    status = "DENY"
                    denied += 1

                    reason = "Policy criteria not met"
                    next_action = "Clinical Denial Review"

            results.append({
                "Request ID": request.get(
                    "request_id"
                ),
                "Member ID": request.get(
                    "member_id"
                ),
                "Member Name": request.get(
                    "patient_name"
                ),
                "Status": status,
                "Missing Information": (
                    ", ".join(missing)
                    if missing
                    else "None"
                ),
                "Reason": reason,
                "Next Action": next_action
            })

        # Dashboard Metrics

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Approved",
            approved
        )

        col2.metric(
            "Pending",
            pending
        )

        col3.metric(
            "Denied",
            denied
        )

        st.subheader(
            "Prior Authorization Results"
        )

        df = pd.DataFrame(results)

        st.dataframe(
            df,
            use_container_width=True
        )