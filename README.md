# Patch Prioritisation Engine

MSc Advanced Computer Science Dissertation Project

## Overview

The Patch Prioritisation Engine (PPE) is a Python-based vulnerability prioritisation tool developed to investigate whether combining multiple vulnerability-related signals can produce a different dependency patch prioritisation order than relying on CVSS severity alone.

The engine uses Google's OSV-Scanner to identify vulnerabilities in software dependencies and enriches the results with CVSS scores, EPSS probabilities and CISA Known Exploited Vulnerabilities (KEV) information. These signals are then used to calculate a risk score and assign a patch priority.

## Features

* Scan Python and Node.js project dependencies using OSV-Scanner
* Extract vulnerability and CVSS information from scanner results
* Retrieve EPSS exploitation probabilities
* Check vulnerabilities against the CISA KEV catalogue
* Calculate a combined vulnerability risk score
* Assign vulnerability priority levels
* Export processed vulnerability data to JSON
* Generate human-readable vulnerability reports

## Prioritisation

The PPE risk score combines CVSS severity with EPSS exploitation probability:

`Risk Score = CVSS + (EPSS × 10)`

Vulnerabilities listed in the CISA KEV catalogue receive a Critical priority.

For vulnerabilities not listed in KEV, priority is assigned using the calculated risk score:

| Priority | Condition       |
| -------- | --------------- |
| Critical | Risk score ≥ 15 |
| High     | Risk score ≥ 10 |
| Medium   | Risk score ≥ 7  |
| Low      | Risk score < 7  |

## Repository Structure

```text
datasets/
    benchmark-data/       Evaluation datasets
    sample-projects/      Sample projects

docs/                     Project documentation

evaluation/
    baseline/             Baseline evaluation data
    figures/              Evaluation figures
    real-world-projects/  Projects used for evaluation
    results/              Generated evaluation results

src/
    epss.py               EPSS integration
    exporter.py           Processed JSON export
    kev.py                CISA KEV integration
    main.py               Main PPE pipeline
    parser.py             OSV result parsing and CVSS extraction
    prioritiser.py        Vulnerability prioritisation
    report.py             Human-readable report generation
    scanner.py            OSV-Scanner integration

```

## Processing Pipeline

```text
Project Manifest
      ↓
OSV-Scanner
      ↓
Raw Vulnerability Results
      ↓
JSON Parsing
      ↓
CVSS + EPSS + KEV Enrichment
      ↓
Risk Score Calculation
      ↓
Priority Assignment
      ↓
Processed JSON + Vulnerability Report
```

## Evaluation

The evaluation compares the prioritisation produced by the PPE against a CVSS-only baseline using the same vulnerability data.

The following metrics are calculated:

* **Top-5, Top-10 and Top-20 overlap** – measures how many of the highest-ranked vulnerabilities are shared between the two approaches.
* **Spearman rank correlation** – measures the similarity between the CVSS and PPE rankings.
* **Mean rank change** – measures the average absolute change in vulnerability position.
* **Priority distribution** – compares the number of Critical, High, Medium and Low vulnerabilities under CVSS and PPE prioritisation.

Evaluation results are saved to:

```text
evaluation/results/summary.csv
```

## Requirements

* Python 3.x
* Google OSV-Scanner
* Python dependencies listed in `requirements.txt`

## Running the Project

Run the main PPE pipeline with:

```text
python src/main.py
```

The pipeline scans the configured project, enriches the vulnerability results, calculates priorities and generates the corresponding output files.

The evaluation can be run with:

```text
python evaluation/evaluate.py
```

## Project Status

Completed prototype and evaluation for the MSc Advanced Computer Science dissertation.
