## BitShift 0101 README

BitShift 0101 is a first-person exploration and puzzle game centered around binary conversion challenges. Players navigate a detailed environment, solve binary puzzles to progress, and experience atmospheric interactions with tools like flashlights and walkie-talkies.

---

### Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Controls](#controls)  
- [Main Menu](#main-menu)  
- [Settings](#settings)  
- [Gameplay & Environment](#gameplay--environment)  
  - [Tutorial](#tutorial)  
  - [Binary Elevator Puzzles](#binary-elevator-puzzles)  
- [Development Team](#development-team)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

In **BitShift 0101**, you explore a 3D environment filled with buildings and a central radio tower. Your objective is to ascend through an elevator by solving binary conversion puzzles. Each floor presents a number that must be converted correctly to binary. Mistakes reset your progress for that floor. Once all puzzles on the floor are solved, you can return to the elevator and continue upward.

---

## Features

- **First-Person Movement**  
  - WASD for locomotion  
  - Mouse/Arrow Keys for looking around  
  - Shift to sprint (with a depleting sprint bar)  

- **Interactive Tools**  
  - **Flashlight** (press **F**) to illuminate dark areas  
  - **Walkie-Talkie** (press **Q**) emits static and hints  

- **Binary Conversion Puzzles**  
  - Three puzzles per floor  
  - Receive a decimal number from a podium  
  - Convert it to correct binary (e.g., 11 → 1011)  
  - Incorrect answers reset that floor’s progress  

- **Elevator Mechanic**  
  - Press **E** to interact with elevator panels  
  - Doors close until all puzzles are solved  
  - Progress to the next floor upon completion  

- **Settings Menu**  
  - Two game modes:  
    - **Normal Mode** (default)  
    - **Epic Mode** (unlocked only after full game completion)  
  - Music and sound effects volume sliders  

---

## Getting Started

### Prerequisites

- **Operating System**: Windows 10 or later / macOS / Linux  
- **Processor**: Dual-core CPU (quad-core or higher recommended)  
- **Memory**: 4 GB RAM  
- **Graphics**: DirectX 11–compatible GPU (or equivalent OpenGL support)  
- **Additional**: Unity 2019.4+ runtime (if distributed as a Unity build)

### Installation

1. **Download the Latest Build**  
   - Obtain the executable or packaged build from the project repository’s “Releases” page.

2. **Extract Files (if applicable)**  
   - Unzip the downloaded archive to a folder of your choice.

3. **Run the Game**  
   - On Windows:  
     ```  
     BitShift_0101.exe  
     ```  
   - On macOS/Linux:  
     ```  
     ./BitShift_0101.x86_64  
     ```

4. **Verify Settings**  
   - Launch the game, navigate to **Settings**, and adjust volume levels or verify the default Normal Mode.

---

## Controls

| Action                  | Key(s)                    |
|-------------------------|---------------------------|
| Move Forward            | W                         |
| Move Backward           | S                         |
| Strafe Left             | A                         |
| Strafe Right            | D                         |
| Look / Turn             | Mouse or Arrow Keys       |
| Sprint                  | Shift (holds sprint bar)  |
| Flashlight Toggle       | F                         |
| Pick Up / Use Walkie-Talkie | Q                    |
| Interact (Doors / Puzzles) | E                     |
| Pause / Main Menu       | Esc                       |

- **Sprint Bar**: Visible on the HUD. Depletes while holding Shift.  
- **Flashlight & Walkie-Talkie**: Use in low-light areas or to gather hints via radio static.

---

## Main Menu

Upon launching the game, you will see the main menu with three options:

1. **Play**  
   - Starts or resumes your current play session in Normal Mode (or Epic Mode if unlocked).  

2. **Settings**  
   - Adjust game options (mode selection, volume sliders, etc.).

3. **Exit**  
   - Close the game.

---

## Settings

From the main menu, select **Settings** to access:

- **Game Mode**  
  - **Normal Mode** (default): Available immediately.  
  - **Epic Mode**: Locked until the player completes all floors in Normal Mode.

- **Music Volume**  
  - Slider range 0–100%. Default is 100%.  

- **Sound Effects Volume**  
  - Slider range 0–100%. Default is 100%.

> **Note**: During demos or presentations, volumes may be lowered to allow voice commentary.

---

## Gameplay & Environment

### Tutorial

When you press **Play** for the first time (or select “Tutorial” within the game environment), you will be guided through:

- **Locomotion Practice**  
  - Moving with WASD, looking with mouse/arrow keys.  
  - Sprinting with Shift to observe the sprint bar behavior.  

- **Tool Usage**  
  - Press **F** to toggle your flashlight in dimly-lit areas.  
  - Press **Q** to pick up a walkie-talkie that emits radio static—useful for atmospheric effect and potential hints.

The tutorial area is designed to familiarize you with basic movement, flashlight mechanics, and the walkie-talkie prop. Once you exit the tutorial zone, you will arrive at the elevator lobby.

---

### Binary Elevator Puzzles

Each floor of the elevator contains:

1. **Observation Area**  
   - You arrive on a floor with open elevator doors.  
   - A crate (or podium) holds a device that displays a **decimal number**.

2. **Puzzle Interaction**  
   - Approach the podium/panel and press **E** to interact.  
   - A decimal number appears (for example, **11**).  
   - You must type the correct binary representation (for 11, type `1011`).

3. **Progress & Reset Mechanic**  
   - Each floor has **three** distinct puzzle stations.  
   - Solve all three correctly to unlock the elevator doors.  
   - If you submit a wrong binary value at any station, your progress on **that floor** resets—you must re-solve all three puzzles.  

4. **Advancing Floors**  
   - After solving all three, exit the floor and return to the elevator.  
   - Press **E** at the elevator panel to ride to the next level (doors open automatically once unlocked).  
   - Repeat the process with new decimal prompts.

Example puzzle sequence on Floor 1:

1. Station A: Decimal **11** → Answer `1011`  
2. Station B: Decimal **6**  → Answer `0110`  
3. Station C: Decimal **13** → Answer `1101`  
4. Station D: Decimal **10** → Answer `1010`  

> The above is illustrative; actual numbers may vary floor by floor.  

**Tip:** Think of basic powers of 2 (1, 2, 4, 8, 16, …) when converting decimals to binary.
