# ClauseGuard: Contract Risk Triage Workflow

The following table summarizes performance compared to a keyword baseline:

## Evaluation Results

| Contract | Expected Result | Keyword Baseline | ClauseGuard Result | Winner |
|---|---|---|---|---|
| safe_contract.txt | Low risk | Found obvious clauses only | Low risk | Tie |
| risky_contract.txt | High risk | Found some keywords but no priority ranking | High risk | ClauseGuard |
| paraphrased_contract.txt | Medium risk | Missed paraphrased clauses | Medium risk | ClauseGuard |

---

## Context, User, and Problem

Small-business procurement teams often need to review multiple vendor contracts quickly before approval.

Currently, this process is manual:
- contracts are reviewed one by one
- clauses are identified inconsistently
- risk prioritization is not standardized

This project introduces a semi-automated workflow that:
1. processes multiple contracts at once  
2. extracts key clause signals  
3. applies consistent risk rules  
4. prioritizes contracts for review  

The goal is not to replace human judgment, but to standardize and accelerate first-pass contract triage.

---

## What I Built

I built a Streamlit-based contract triage tool that processes multiple contracts, extracts key clause signals, applies rule-based risk evaluation, and outputs a prioritized decision table for review.

---

## Why GenAI Is Useful

GenAI-style extraction is useful because contract clauses are often expressed in varied or paraphrased language.

A keyword baseline may fail when:
- clauses are reworded  
- indirect phring is used  
- legal language is less standardized  

This system simulates GenAI-style understanding by detecting meaning beyond exact keywords (e.g., "end this agreement" vs "termination clause").

This improves clause detection robustness compared to keyword-only approaches.

While this project uses simplified logic for demonstration, it reflects how GenAI systems can generalize beyond exact keyword matching in real applications.

---

## Baseline

The baseline is keyword search for terms such as termination, liability, indemnification, auto-renewal, and governing law.

---

## Evaluation

I tested the system on three representative contract types:
- a safe contract with standard clauses  
- a risky contract with missing or problematic clauses  
- a paraphrased contract with non-standard wording  

Results show:
- the keyword baseline fails to detect paraphrased clauses  
- ClauseGuard correctly identifies clause signals and assigns appropriate risk levels  
- the system produces consistent prioritization across contracts  

This demonstrates improved robustness compared to keyword-only approaches.

---

## What Worked

The system successfully distinguishes between high, medium, and low risk contracts and prioritizes them for review. It also performs better than the keyword baseline in detecting paraphrased clauses.

---

## What Failed / Limitations

The current system uses simplified rule logic and sample text files. It may fail on complex legal language, long contracts, or ambiguous phrasing. It may also misclassify contracts if key clauses are expressed in uncommon ways.

---

## Human Involvement

This tool is designed as a first-pass triage system. Human reviewers are still required to:
- validate clause interpretations  
- make final legal decisions  
- handle edge cases or ambiguous contracts  

---

## Why This Is Not Just ChatGPT

While ChatGPT can analyze a single contract at a time, this project focuses on workflow automation rather than one-off analysis.

Key differences:
- batch processing of multiple contracts  
- consistent rule-based risk evaluation  
- standardized structured outputs  
- automatic prioritization for decision-making  

This creates a repeatable and scalable process, rather than relying on manual, one-by-one ChatGPT queries.

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py