# Log Report - Harbor Terminal-Bench Task

## Overview

This project is a corrected Harbor Terminal-Bench 2 (TB2) task that parses an Apache-style access log and generates a JSON summary report.

The original task contained several authoring issues related to task configuration, environment reproducibility, verifier correctness, and task instructions. These issues have been fixed to make the task reproducible and correctly graded.

---

## Project Structure

```
log-report/
├── access.log
├── task.toml
├── instruction.md
├── environment/
│   └── Dockerfile
├── solution/
│   ├── solve.py
│   └── solve.sh
├── tests/
│   ├── test_outputs.py
│   └── test.sh
└── README.md
```

---

## Task Description

The task reads an Apache-style access log located at:

```
/app/access.log
```

and generates:

```
/app/report.json
```

The JSON report contains:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

---

## Success Criteria

The solution must:

1. Read `/app/access.log`.
2. Count the total number of requests.
3. Count the number of unique client IP addresses.
4. Determine the most frequently requested URL path.
5. Write the results to `/app/report.json`.

---

## Improvements Made

### Task Configuration

- Corrected `artifacts` to a top-level array.
- Updated the artifact path to `/app/report.json`.
- Disabled unnecessary internet access.

### Environment

- Removed the leaked reference solution from the runtime environment.
- Updated the Docker configuration for reproducible builds using a pinned base image.

### Verifier

- Added validation of JSON contents instead of only checking file existence.
- Added one test for each success criterion.
- Updated the verifier to produce Harbor-compatible outputs.

### Instructions

- Rewrote `instruction.md`.
- Added clear numbered success criteria.
- Ensured the instructions exactly match the verifier.

---

## Running

Oracle solution:

```bash
harbor run -p log-report -a oracle
```

No-op agent:

```bash
harbor run -p log-report --agent nop
```

Expected results:

| Run | Reward |
|-----|--------|
| Oracle | 1 |
| NOP Agent | 0 |

---

## Technologies

- Python 3
- Docker
- Harbor TB2
- Pytest

---

## License

This project was created for educational purposes as part of a Harbor Terminal-Bench authoring assessment.
