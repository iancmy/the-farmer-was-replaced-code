# **The Farmer Was Replaced Code**

This repository contains my collection of Python scripts designed to run within
the game _The Farmer Was Replaced_.

## **📋 Prerequisites**

- **Game**: _The Farmer Was Replaced_ (v1.0 or higher recommended).
- **Unlocks Required**:
  - Unlocks.Senses (for grid awareness)
  - Unlocks.Variables & Unlocks.Functions
  - Unlocks.Multi_Trade (for efficient buying)
  - Unlocks.Mazes (for rmove navigation)

## **📥 Installation & Setup**

1. **Clone the Repository**:
   `git clone https://github.com/iancmy/the-farmer-was-replaced-automation.git`

2. **Importing to Game**:
   - Open the game's built-in code editor.
   - Copy the contents of the .py files into the corresponding in-game scripts.
   - Ensure moves.py is present if you are importing main.py.

3. **Running the Bot**:
   - Select main.py as your active script.
   - Press the **Run** button (usually F5 in the game).

## **Usage**

The main control loop is located in main.py. You can toggle specific farming
behaviors by uncommenting the desired functions in the main() block:

```python
def main():
  while True:
    buy_pumpkin_seed()
    buy_carrot_seed()
    # plant_grass()   # Uncomment to farm Hay
    plant_tree()
    # plant_pumpkin() # Uncomment for Pumpkin
```
