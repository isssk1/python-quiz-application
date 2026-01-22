# COM4402 – Python Quiz Application  
## Manual Test Cases

**Student Name:** Issa Khan  
**Student Number:** 2421170  
**Module Code:** COM4402  

---

## Testing Overview
The quiz application was tested using **manual testing** to verify correctness, input validation, score calculation, and program termination.  
The following test cases cover:
- Normal usage
- Incorrect and invalid inputs
- Edge cases
- Program start and end behavior

All tests were executed using Python 3 via the command line.

---

## Test Case TC01

| Field | Description |
|------|------------|
| **Test ID** | TC01 |
| **Description** | Start quiz normally |
| **Input Data** | Run the program |
| **Expected Outcome** | Quiz starts and displays welcome message |
| **Actual Outcome** | Quiz started successfully and welcome message displayed |
| **Result** | Pass |

---

## Test Case TC02

| Field | Description |
|------|------------|
| **Test ID** | TC02 |
| **Description** | Correct answer input |
| **Input Data** | Enter correct option number |
| **Expected Outcome** | “Correct!” message displayed and score increases |
| **Actual Outcome** | Correct message displayed and score updated |
| **Result** | Pass |

---

## Test Case TC03

| Field | Description |
|------|------------|
| **Test ID** | TC03 |
| **Description** | Incorrect answer input |
| **Input Data** | Enter wrong option number |
| **Expected Outcome** | “Incorrect.” message displayed and score remains unchanged |
| **Actual Outcome** | Incorrect message displayed and score unchanged |
| **Result** | Pass |

---

## Test Case TC04

| Field | Description |
|------|------------|
| **Test ID** | TC04 |
| **Description** | Invalid input – letter |
| **Input Data** | Enter `a` |
| **Expected Outcome** | Error message shown and user re-prompted |
| **Actual Outcome** | Invalid input message shown and user re-prompted |
| **Result** | Pass |

---

## Test Case TC05

| Field | Description |
|------|------------|
| **Test ID** | TC05 |
| **Description** | Invalid input – number out of range |
| **Input Data** | Enter `5` |
| **Expected Outcome** | Error message shown and user re-prompted |
| **Actual Outcome** | Invalid input message shown and user re-prompted |
| **Result** | Pass |

---

## Test Case TC06

| Field | Description |
|------|------------|
| **Test ID** | TC06 |
| **Description** | Edge case – lowest valid input |
| **Input Data** | Enter `1` |
| **Expected Outcome** | Input accepted |
| **Actual Outcome** | Input accepted successfully |
| **Result** | Pass |

---

## Test Case TC07

| Field | Description |
|------|------------|
| **Test ID** | TC07 |
| **Description** | Edge case – highest valid input |
| **Input Data** | Enter `4` |
| **Expected Outcome** | Input accepted |
| **Actual Outcome** | Input accepted successfully |
| **Result** | Pass |

---

## Test Case TC08

| Field | Description |
|------|------------|
| **Test ID** | TC08 |
| **Description** | Multiple incorrect attempts before valid input |
| **Input Data** | Enter `x`, then `7`, then `2` |
| **Expected Outcome** | Program continues safely without crashing |
| **Actual Outcome** | Program handled inputs correctly and accepted valid input |
| **Result** | Pass |

---

## Test Case TC09

| Field | Description |
|------|------------|
| **Test ID** | TC09 |
| **Description** | Score calculation accuracy |
| **Input Data** | Answer 3 questions correctly and 2 incorrectly |
| **Expected Outcome** | Final score displayed as `3 / 5` |
| **Actual Outcome** | Final score displayed correctly |
| **Result** | Pass |

---

## Test Case TC10

| Field | Description |
|------|------------|
| **Test ID** | TC10 |
| **Description** | Program termination |
| **Input Data** | Complete all questions |
| **Expected Outcome** | Final score displayed and program ends |
| **Actual Outcome** | Program ended correctly after displaying final score |
| **Result** | Pass |

---

## Summary
All test cases passed successfully.  
The program handled valid inputs, invalid inputs, edge cases, scoring, and termination without errors.
