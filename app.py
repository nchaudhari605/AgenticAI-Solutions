import streamlit as st

from agents.intake import intake_agent
from agents.validation import validation_agent
from agents.policy import policy_agent
from agents.recommendation import recommendation_agent
from agents.communication import communication_agent

st.title(
    "AI Prior Authorization Copilot By Narendra"
)

uploaded_file = st.file_uploader(
    "Upload Prior Authorization Request"
)

if uploaded_file:

    document = uploaded_file.read().decode()

    st.success(
        "Document Uploaded"
    )

    if st.button(
        "Analyze Request"
    ):

        st.write(
            "✅ Intake Agent Running"
        )

        intake_result = intake_agent(
            document
        )

        st.write(
            "✅ Validation Agent Running"
        )

        missing = validation_agent(
            intake_result
        )

        st.write(
            "✅ Policy Agent Running"
        )

        policy = policy_agent()

        st.write(
            "✅ Recommendation Agent Running"
        )

        recommendation = recommendation_agent(
            intake_result,
            policy
        )

        st.subheader(
            "Missing Information"
        )

        st.write(
            missing
        )

        st.subheader(
            "AI Recommendation"
        )

        st.write(
            recommendation
        )

        st.write(
            "✅ Communication Agent Running"
        )

        communication = communication_agent(
            document,
            recommendation
        )

        st.subheader(
            "Member / Provider Communication"
        )

        st.text(
            communication
        )