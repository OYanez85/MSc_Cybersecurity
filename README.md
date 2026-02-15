# MSc Cybersecurity Thesis Artifact  
## Deterministic Governance for Injection-Resilient LLM Agent Architectures

---

## Overview

This repository contains the experimental artifact developed for the MSc dissertation:

**“Deterministic Governance for Injection-Resilient LLM Agent Architectures”**

The project demonstrates how a hybrid security architecture — combining semantic sanitization (RAG filtering) and deterministic policy enforcement — mitigates injection-based attacks in LLM-powered agent systems.

The artifact is fully local, reproducible, and designed for academic evaluation.

---

## Research Objective

Modern LLM agents can execute tools (e.g., send emails, query databases).  
This introduces a structural risk:

> Data can be transformed into control.

This project evaluates whether introducing a deterministic policy layer before tool execution reduces attack surface in agentic systems.

---

## Architecture

The system implements a **defense-in-depth model**:

### 1️⃣ RAG Sanitization Layer
- Neutralizes malicious instructions in retrieved content.
- Prevents tool activation via prompt injection.

### 2️⃣ PolicyEngine (Deterministic Governance Layer)
- Validates tool-calls before execution.
- Blocks:
  - Prompt injection
  - RAG injection
  - SQL injection
  - Data exfiltration attempts

### 3️⃣ Isolated Tool Runtime
- Simulated execution environment.
- No real external side effects.

---

## Project Structure

thesis_artifact/
│
├── agent.py              # Simulated LLM decision layer  
├── policy.py             # Deterministic PolicyEngine  
├── runner.py             # Experimental execution script  
│  
├── tools/  
│   ├── runtime.py        # Simulated tools  
│   └── schemas.py        # ToolCall data model  
│  
├── rag/  
│   ├── filter.py         # RAG sanitization layer  
│   └── ingest.py         # Knowledge base ingestion  
│  
├── logs/                 # Structured execution logs (JSONL)  
└── reports/              # Experimental summaries  

---

## Installation

```bash
cd thesis_artifact
python3 -m venv .venv
source .venv/bin/activate
```
No external dependencies are required.

## Running the Experiment

### Default execution

```bash
python runner.py
```
## With RAG filter comparison

```bash
python runner.py --out with_filter
python runner.py --no-rag-filter --out no_filter
```
## Multiple experimental runs

```bash
python runner.py --runs 50 --out with_filter_50
python runner.py --no-rag-filter --runs 50 --out no_filter_50
```
## Experimental Results

The system evaluates four attack scenarios:

- Prompt Injection
- RAG Injection
- SQL Injection
- Legitimate Tool Execution

## 50-Run Configuration Results
Mode	          Tool Calls	Blocked	Prevented
With RAG Filter	       150	  100	     50
Without Filter	       200	  150	      0

## Security Model

This project formalizes a separation principle:

- Inference remains probabilistic
- Execution remains deterministic
- Authority is explicitly governed

## This design is suitable for regulated environments such as:

- Healthcare
- Insurance
- Banking
- Public sector

## Reproducibility

- Fully local execution
- No external APIs
- Structured JSONL logs
- Deterministic decision engine
- Quantifiable security metrics

## License

Academic research artifact.
For evaluation and educational purposes.

## Author

Oscar Yanez
MSc Cybersecurity Dissertation Project
