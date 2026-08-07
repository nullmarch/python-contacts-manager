# python-contacts-manager
learning project
## About 
A command-line contacts manager built in python as part of my self-directed programming study.

## Features
- Add contacts with duplicates detection
- Search contacts by name or phone number
- View all saved contacts
- Input validation
- Delete contacts with confirmation prompt
- Modify contacts with selective field updating — leave a field empty to keep existing value

## What I Learned 

Through building and debugging this project I worked through 
several non-obvious programming concepts:

- **Boolean flag pattern** — using a flag variable set inside 
  a loop with decisions made outside, preventing premature 
  actions before all iterations complete
  
- **Loop scope** — understanding when to declare and reset 
  variables inside vs outside loops to prevent state 
  carrying between sessions

- **Truthiness in Python** — lists and dictionaries evaluate 
  as True when populated and False when empty, enabling 
  clean conditional checks

- **Duplicate detection logic** — implementing a full scan 
  before any write operation using boolean flags rather than 
  acting on first match

- **Input validation** — stripping whitespace to prevent 
  empty strings being stored as valid data

- **Functions and parameters** — refactored each task into its own function, 
  passing the contacts list as a parameter to give functions access to shared data
  
- **Scope** — functions can only see variables passed to them or declared inside them

- **Mutable objects as parameters** — lists passed to functions are not copied, 
  the function gets direct access to the original, so changes persist after the function ends

## Bugs Fixed During Development

**1. Duplicate check not iterating**
- Checking a single `contact` dict instead of looping through `contacts` list
- Fix: `for contact in contacts`

**2. Wrong boolean operator in duplicate condition**
- `or` was letting duplicates through when only one field matched
- Fix: `and` to add only when neither name nor phone exists

**3. Adding inside the loop**
- Contact was added on first non-matching iteration without checking remaining contacts
- Fix: boolean flag `duplicate_found`, set inside loop, add decision made outside loop

**4. `duplicate_found` not resetting**
- Declared outside while loop, permanently `True` after first duplicate attempt
- Fix: reset to `False` inside `if task == 'add'` before the for loop

**5. Search "not found" printing per iteration**
- Printing inside loop caused false negatives on non-matching iterations
- Fix: boolean flag + variable to store match, print decision after loop

**6. Counter not resetting in view**
- Counter declared outside the task block, kept incrementing across sessions
- Fix: reset counter to `0` inside `elif task == 'view'` before the loop

**7. Empty input accepted**
- Empty string stored as valid contact
- Fix: `if name.strip() == "" or phone.strip() == "": continue`-

**8. Confirmation input not normalized** — fixed by applying .lower().strip() to user confirmation input

**9. Boolean flag reset inside loop** — initial delete implementation reset contact_found to False on non-matching iterations, fixed by removing else clause from loop
