# quantum-pulse-scanner# ⚛️ Quantum-Pulse: Cryptographic Agility & Shor's Algorithm Vulnerability Scanner

A next-generation Cryptographic Posture & Post-Quantum Cryptography (PQC) readiness scanner designed to audit source code for classical public-key cryptography vulnerable to **Shor's Algorithm** (RSA, ECC, ECDH) and symmetric bit-strength degradation via **Grover's Algorithm**.

---

## ✨ Features
- **Quantum Threat Heuristics**: Identifies asymmetric cryptographic primitives vulnerable to polynomial-time factorization on Cryptographically Relevant Quantum Computers (CRQCs).
- **NIST FIPS 203/204/205 Standards Mapping**: Maps identified legacy ciphers directly to official NIST PQC alternatives (**ML-KEM**, **ML-DSA**, and **SLH-DSA**).
- **Quantum CBOM Generation**: Automatically generates a machine-readable **Cryptographic Bill of Materials (CBOM)** JSON artifact.
- **Quantum Readiness Scoring**: Calculates a normalized quantum agility index (`0–100%`) for enterprise DevSecOps pipelines.
- **Zero Third-Party Dependencies**: Pure Python standard library implementation.

---

## 🚀 Quick Start
```bash
python3 quantum_pulse.py legacy_enterprise_app.py
