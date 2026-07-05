# Context-Aware Vulnerability Prioritisation Engine

MSc Advanced Computer Science Dissertation Project

## Overview

This project investigates whether contextual information can improve the prioritisation of software dependency vulnerabilities compared to traditional severity-based approaches.

The implementation uses Google's OSV-Scanner as the vulnerability discovery engine and extends it with a context-aware prioritisation framework that incorporates additional vulnerability intelligence and dependency information.

## Objectives

- Detect vulnerable dependencies using OSV-Scanner
- Enrich vulnerability data with additional security context (e.g., EPSS and CISA KEV)
- Generate prioritised patch recommendations
- Evaluate the proposed approach against existing prioritisation methods

## Repository Structure

```
docs/            Project documentation
src/             Source code
datasets/        Evaluation datasets
evaluation/      Experimental results
output/          Generated reports
test-projects/   Sample vulnerable projects
tests/           Unit tests
```

## Status

🚧 Work in progress
