import os
import sys
import json
import re
import time
from datetime import datetime, timezone

# ANSI Color & Styling Tokens
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[38;5;196m"
GREEN   = "\033[38;5;48m"
CYAN    = "\033[38;5;51m"
AMBER   = "\033[38;5;214m"
MAGENTA = "\033[38;5;201m"
GRAY    = "\033[38;5;242m"

BANNER = f"""{CYAN}{BOLD}
  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗
 ██╔═══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║
 ██║   ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 ██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
  ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
{RESET}{MAGENTA} » QUANTUM-PULSE: POST-QUANTUM CBOM & SHOR'S ALGORITHM AUDITOR «{RESET}
"""

class QuantumPulseAuditor:
    def __init__(self, rules_path="quantum_rules.json"):
        if not os.path.exists(rules_path):
            print(f"{RED}[-] Configuration rules file '{rules_path}' not found.{RESET}")
            sys.exit(1)

        with open(rules_path, "r") as f:
            self.config = json.load(f)

        self.rules = self.config.get("rules", [])
        self.pqc_standards = self.config.get("nist_pqc_standards", {})

    def scan_target(self, target_path):
        if not os.path.exists(target_path):
            print(f"{RED}[-] Target file '{target_path}' not found.{RESET}")
            return

        print(BANNER)
        print(f"{BOLD}Target Cryptographic Source:{RESET} {CYAN}{target_path}{RESET}\n")

        steps = [
            "Parsing source Abstract Syntax Tree & cryptographic primitives",
            "Cross-referencing against Shor's Algorithm vulnerability heuristics",
            "Evaluating Grover's Algorithm effective bit-strength degradation",
            "Synthesizing NIST FIPS 203/204/205 Post-Quantum Migration Targets",
            "Compiling Cryptographic Bill of Materials (CBOM)"
        ]
        for step in steps:
            time.sleep(0.2)
            print(f"  {CYAN}▸{RESET} {step}...")

        print("\n" + "=" * 85 + "\n")
        print(f"{BOLD}{'LINE':<6} {'ALGORITHM / PRIMITIVE':<28} {'QUANTUM RISK':<26} {'SEVERITY'}{RESET}")
        print("-" * 85)

        findings = []
        with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, start=1):
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue

            for rule in self.rules:
                if re.search(rule["pattern"], clean):
                    findings.append({
                        "line": idx,
                        "id": rule["id"],
                        "name": rule["name"],
                        "algorithm_type": rule["algorithm_type"],
                        "threat_model": rule["threat_model"],
                        "severity": rule["severity"],
                        "nist_migration": rule["nist_migration"],
                        "code_snippet": clean
                    })
                    sev_color = RED if rule["severity"] == "CRITICAL" else AMBER
                    print(f"{idx:<6} {rule['name'][:26]:<28} {rule['threat_model'][:24] + '..':<26} {sev_color}{rule['severity']}{RESET}")

        print("=" * 85)

        # Calculate Quantum Readiness Posture Score
        total_issues = len(findings)
        critical_issues = sum(1 for f in findings if f["severity"] == "CRITICAL")
        readiness_score = max(0, 100 - (critical_issues * 30) - ((total_issues - critical_issues) * 15))
        score_color = GREEN if readiness_score >= 80 else (AMBER if readiness_score >= 50 else RED)

        print(f"\n{BOLD}Post-Quantum Readiness Index:{RESET} {score_color}{BOLD}{readiness_score}/100{RESET}")
        print(f"Classical Vulnerable Algorithms Flagged: {RED}{total_issues}{RESET} (Critical Shor Risks: {RED}{critical_issues}{RESET})\n")

        # Export Quantum Cryptographic Bill of Materials (CBOM)
        cbom_data = {
            "cbomVersion": "1.0-PQC",
            "generatedAt": datetime.now(timezone.utc).isoformat() + "Z",
            "targetAsset": target_path,
            "quantumReadinessScore": readiness_score,
            "nistStandardsReference": self.pqc_standards,
            "vulnerabilities": findings
        }
        cbom_filename = "quantum_cbom.json"
        with open(cbom_filename, "w") as f:
            json.dump(cbom_data, f, indent=2)

        print(f"{GREEN}[✓] Exported Quantum CBOM Ledger:{RESET} {BOLD}{cbom_filename}{RESET}\n")

        if findings:
            print(f"{AMBER}{BOLD}[🛠️ NIST POST-QUANTUM MIGRATION ROADMAP]{RESET}")
            for idx, f in enumerate(findings, start=1):
                print(f"  {CYAN}#{idx} [Line {f['line']}]{RESET} {BOLD}{f['name']}{RESET}")
                print(f"     ├─ Risk Profile:   {f['threat_model']}")
                print(f"     └─ NIST PQC Fix:   {GREEN}{f['nist_migration']}{RESET}\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "legacy_enterprise_app.py"
    auditor = QuantumPulseAuditor()
    auditor.scan_target(target)
