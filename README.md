# Bus Complaint Sorter

A console-based Python capstone project for classifying college bus complaints, extracting route numbers, flagging safety-related complaints and creating reports.

## Features
- Reads `complaints.csv` and `routes.csv`.
- Uses an LLM API to classify complaints.
- Checks the model's JSON response.
- Checks route numbers using Python.
- Retries invalid responses once, then marks them `needs_manual_review`.
- Creates `results.csv`, `urgent.csv` and `summary.txt`.
- Keeps final decisions with the human transport officer.

## Requirements
- Python 3.10 or later
- Internet connection and a provider API key for LLM mode

## Setup in VS Code

1. Open this project folder in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment:
   - Windows: `py -m venv .venv`
   - macOS/Linux: `python3 -m venv .venv`
4. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows Command Prompt: `.venv\Scripts\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
5. Install packages: `python -m pip install -r requirements.txt`
6. Copy `.env.example` to a new file named `.env`.
7. Add your own API key to `.env`. Never share or commit this file.
8. Run: `python main.py`

## Offline demonstration

To test the CSV workflow without an API call, set `DEMO_MODE=true` in `.env`, then run `python main.py`. This uses a simple rule-based demonstration classifier. It is not the LLM and must not be presented as an LLM test.

## Run validator tests

Run `python evaluate.py`. These tests check the Python validator, not the LLM's accuracy.

## Output files
- `results.csv`: one row per complaint.
- `urgent.csv`: complaints flagged as safety-related.
- `summary.txt`: category counts, route counts and safety list.

## Important safety rule
The application does not contact drivers, decide who is at fault, or take action. The transport officer reviews safety complaints and makes decisions.

## Before submission
Use your real college route data, run real LLM tests, record measured latency/cost, complete your decision journal and write your own 400-word reflection. Confirm with faculty that the chosen API provider is acceptable.
