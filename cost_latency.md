# Cost and Latency Note

## API calls
The program makes one LLM call per complaint in the normal case. If a response is invalid or the request fails, it retries once. Therefore:

- Normal case: N calls for N complaints.
- Maximum under this retry rule: 2N calls.
- For 20 complaints: about 20 calls normally, at most 40 calls.

## Latency
Measure the average response time using a stopwatch or timestamps during an actual run. Record the observed average and total time here:
- Average time per call: [fill in after running]
- Total run time for your test file: [fill in after running]

## Cost
API prices, free-tier limits and model availability can change. Do not claim the project is free or enter an invented price. Check the provider's current pricing and usage dashboard on the date of your test. Record:
- Model used: [fill in]
- Input tokens: [fill in from provider dashboard]
- Output tokens: [fill in from provider dashboard]
- Estimated total cost: [fill in from provider dashboard]

The offline DEMO_MODE does not call an LLM and has no API usage cost. It is only for testing the file workflow, not for measuring LLM accuracy.
