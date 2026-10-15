import streamlit as st
import pandas as pd
import os

from agents.intake import intake_agent
from agents.validation import validation_agent
from agents.policy import policy_agent
from agents.recommendation import recommendation_agent

st.title("AI Prior Authorization Batch Processing")

REQUEST_FOLDER = "requests"

if st.button("Process All Requests"):

    approved = 0
    pending = 0
    denied = 0

    results = []

    policy = policy_agent()

    files = os.listdir(REQUEST_FOLDER)

    for file in files:

        filepath = os.path.join(
            REQUEST_FOLDER,
            file
        )

        with open(filepath, "r") as f:
            document = f.read()

        intake_result = intake_agent(
            document
        )

        missing = validation_agent(
            intake_result
        )

        recommendation = recommendation_agent(
            intake_result,
            policy
        )

        if "APPROVE" in recommendation:
            status = "APPROVE"
            approved += 1

        elif "PEND" in recommendation:
            status = "PEND"
            pending += 1

        else:
            status = "DENY"
            denied += 1

        # Business-friendly reason/action

        if missing:

            reason = "Required documentation is missing"

            next_action = "Provider Outreach"

        elif status == "APPROVE":

            reason = "All policy criteria met"

            next_action = "Ready For Human Review"

        else:

            reason = "Policy criteria not met"

            next_action = "Clinical Denial Review"

        results.append({
            "File": file,
            "Status": status,
            "Missing Information": (
                ", ".join(missing)
                if missing
                else "None"
            ),
            "Reason": reason,
            "Next Action": next_action
        })

    # Summary Metrics

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

    df = pd.DataFrame(
        results
    )

    st.dataframe(
        df,
        use_container_width=True
    )