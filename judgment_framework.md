# Judgment Framework

| Part of the tool | Cost of being wrong | Can it be verified without AI? | Who is accountable / human checkpoint? |
|---|---|---|---|
| Category classification | Complaint may be counted under the wrong type | A person can read the original complaint | Project user checks unclear cases |
| Urgent safety flag | A safety issue may not be prioritised | Transport officer can inspect the complaint and confirm | Transport officer reviews every urgent item |
| Route extraction | Complaint may be assigned to the wrong route | Python checks routes.csv and the original text | Python performs rule check; staff confirm uncertain cases |
| Summary | Important context may be omitted | Compare summary with original complaint | Human reviewer checks before action |
| Category and route counts | Reports may be misleading | Python counts validated rows | Project user checks report output |
| Final action | Wrong action may affect students or staff | Requires real-world investigation | Transport officer alone decides; tool never acts independently |

## Human checkpoint
All safety complaints are sent to the transport officer for review. The application does not contact drivers, decide fault, or take action on its own.
