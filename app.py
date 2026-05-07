import streamlit as st
import pandas as pd

CLAUSES = ["termination", "liability", "indemnification", "auto-renewal", "governing law"]

def keyword_baseline(text):
    text_lower = text.lower()
    results = {}
    for clause in CLAUSES:
        results[clause] = "Found" if clause in text_lower else "Missing"
    return results

def fake_genai_extract(text):
    text_lower = text.lower()

    results = {
        "termination": "Present" if (
            "termination" in text_lower
            or "terminate" in text_lower
            or "end this agreement" in text_lower
            or "written notice" in text_lower
        ) else "Missing",

        "liability": "Unlimited" if (
            "unlimited liability" in text_lower
            or "no limitation of liability" in text_lower
        ) else ("Limited" if "liability" in text_lower else "Unclear"),

        "indemnification": "Present" if (
            "indemnification" in text_lower
            or "hold harmless" in text_lower
            or "indemnify" in text_lower
        ) else "Missing",

        "auto-renewal": "Present" if (
            "auto-renewal" in text_lower
            or "automatically renew" in text_lower
            or "automatic renewal" in text_lower
        ) else "Missing",

        "governing law": "Present" if (
            "governing law" in text_lower
            or "laws of" in text_lower
            or "law of" in text_lower
        ) else "Missing"
    }

    return results

def apply_risk_rules(extracted):
    risk = "Low"
    reasons = []

    if extracted["termination"] == "Missing":
        risk = "High"
        reasons.append("Termination clause is missing.")

    if extracted["liability"] == "Unlimited":
        risk = "High"
        reasons.append("Liability appears unlimited.")

    if extracted["auto-renewal"] == "Present":
        if risk != "High":
            risk = "Medium"
        reasons.append("Auto-renewal clause may require review.")

    if extracted["governing law"] == "Missing":
        if risk == "Low":
            risk = "Medium"
        reasons.append("Governing law clause is missing.")

    if not reasons:
        reasons.append("No major risk flags detected by the rule engine.")

    return risk, " ".join(reasons)

st.title("ClauseGuard: Contract Clause Extraction and Risk Triage Tool")

st.write(
    "Upload vendor contract text files. The app extracts key clauses, applies simple risk rules, "
    "and prioritizes contracts for human review."
)

uploaded_files = st.file_uploader(
    "Upload contract .txt files",
    type=["txt"],
    accept_multiple_files=True
)

if st.button("Run Clause Review"):
    if not uploaded_files:
        st.warning("Please upload at least one contract file.")
    else:
        rows = []

        for file in uploaded_files:
            text = file.read().decode("utf-8", errors="ignore")

            baseline = keyword_baseline(text)
            extracted = fake_genai_extract(text)
            risk, recommendation = apply_risk_rules(extracted)

            rows.append({
                "Contract": file.name,
                "Overall Risk": risk,
                "Recommendation": recommendation,
                "Termination": extracted["termination"],
                "Liability": extracted["liability"],
                "Indemnification": extracted["indemnification"],
                "Auto-Renewal": extracted["auto-renewal"],
                "Governing Law": extracted["governing law"],
                "Keyword Baseline Summary": str(baseline)
            })

        df = pd.DataFrame(rows)

        risk_order = {"High": 0, "Medium": 1, "Low": 2}
        df["Risk Order"] = df["Overall Risk"].map(risk_order)
        df = df.sort_values("Risk Order").drop(columns=["Risk Order"])

        st.subheader("Prioritized Contract Risk Results")
        st.dataframe(df)

        st.subheader("Business Interpretation")
        st.write(
            "Contracts marked High should be reviewed first by a human reviewer or legal support. "
            "Medium-risk contracts should be checked before approval. Low-risk contracts may proceed "
            "after normal business review."
        )