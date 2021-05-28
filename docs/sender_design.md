## Tasks

### System boundaries

| Item                              | Included?     | Reasoning / Assumption
|-----------------------------------|---------------|---
2 BMS params generation             | Yes           | Part of the software requirements
Param accumulation in stream        | Yes           | Part of the software requirements
Stream Console Output               | Yes           | Part of the software requirements
Quit Stream on User Input           | Yes           | Part of the software requirements
BMS param validation                | No            | Params generated and sent as is. Assume input validation elsewhere
Param reception acknowledgement     | No            | Leads to assumptions on receiver and stream capabilities

### Test cases

1. Generate "Invalid Input" output when the generated parameter data could not be parsed from source
1. Generate "No Input" output when the parameter generation yields no data
1. Generate "Format error" when output stream cannot be formed in the desired format
1. Validate stream output in the desired format for a given param generator
1. Validate quit stream when a quit event is sent to the stream generation

### Fakes and Reality

| Functionality            | Input                            | Output                     | Faked/mocked part
|--------------------------|----------------------------------|----------------------------|-----------------------------
Read param from source     | Sensor data stream               | internal data-structure    | Faked the stream source
Validate input             | internal data-structure          | valid / invalid / no data  | None - it's a pure function
Convert to output format   | internal data-structure          | Stream in selected format  | Faked a JSON/Custom formatter
Validate output            | Stream in selected format        | valid / invalid            | None - it's a pure function
Send data on console       | Stream in selected format        | minimum, maximum values    | Mock the console std output
Ensure graceful quit       | Quit Event                       | Quit Confirmation          | None - it's a pure function