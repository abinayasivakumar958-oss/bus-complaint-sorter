"""Small offline evaluation harness for the validator and route checker."""
from main import is_valid

routes = {4: "Medavakkam", 7: "Chromepet", 2: "Velachery"}

tests = [
    {
        "name": "Late bus",
        "complaint": "Route 4 bus arrived late",
        "result": {"category": "delay", "urgent": False, "route": 4, "summary": "Route 4 bus arrived late"},
        "expected_valid": True
    },
    {
        "name": "Phone while driving",
        "complaint": "Driver on route 7 used phone while driving",
        "result": {"category": "driver", "urgent": True, "route": 7, "summary": "Driver used phone while driving"},
        "expected_valid": True
    },
    {
        "name": "Invented route",
        "complaint": "The bus is crowded",
        "result": {"category": "crowding", "urgent": False, "route": 99, "summary": "Bus is crowded"},
        "expected_valid": True
    },
    {
        "name": "Invalid category",
        "complaint": "Route 2 bus is late",
        "result": {"category": "late_bus", "urgent": False, "route": 2, "summary": "Bus is late"},
        "expected_valid": False
    },
    {
        "name": "Summary too long",
        "complaint": "Route 4 bus arrived late",
        "result": {"category": "delay", "urgent": False, "route": 4,
                   "summary": "This is a very long summary that contains more than twelve words in total"},
        "expected_valid": False
    }
]

correct = 0
print("EVALUATION RESULTS")
print("-" * 50)
for test in tests:
    result = test["result"].copy()
    valid, reason = is_valid(result, test["complaint"], routes)
    passed = valid == test["expected_valid"]
    if passed:
        correct += 1
    print(f"{test['name']}: {'PASS' if passed else 'FAIL'} ({reason})")
    if test["name"] == "Invented route":
        print(f"  Route after Python check: {result['route']}")

print(f"\nValidator test score: {correct}/{len(tests)}")
print("Note: These tests check Python validation, not the LLM's classification accuracy.")
