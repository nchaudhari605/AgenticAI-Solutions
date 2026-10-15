def policy_agent():

    with open(
        "policies/mri_policy.txt",
        "r"
    ) as f:

        return f.read()