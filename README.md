# MSc Cybersecurity Thesis Artifact  
## Deterministic Governance for Injection-Resilient LLM Agent Architectures

---

## 📌 Overview

This repository contains the experimental artifact developed for the MSc dissertation:

**“Deterministic Governance for Injection-Resilient LLM Agent Architectures”**

The project demonstrates how a hybrid security architecture — combining semantic sanitization (RAG filtering) and deterministic policy enforcement — mitigates injection-based attacks in LLM-powered agent systems.

The artifact is fully local, reproducible, and designed for academic evaluation.

---

## 🧠 Research Objective

Modern LLM agents can execute tools (e.g., send emails, query databases).  
This introduces a structural risk:

> Data can be transformed into control.

This project evaluates whether introducing a deterministic policy layer before tool execution reduces attack surface in agentic systems.

---

## 🏗 Architecture

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

## 📂 Project Structure

