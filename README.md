Certainly! Below is a suggested README file for your Knee Bend Exercise Rep Counter using Mediapipe:

---

# Knee Bend Exercise Rep Counter

## Overview

This computer vision project utilizes the power of Mediapipe to count successful repetitions of the knee bend exercise. The system employs key features to provide an accurate and user-friendly experience.

## Features

### Rep Counting

- Users can effortlessly count successful rep counts of the knee bend exercise.
- A timer at the top left corner indicates the duration of the knee bend, requiring a hold of at least 8 seconds for a successful rep count.

### Real-time Feedback

- The timer starts as soon as the user bends their knee.
- Upon reaching 8 seconds, the rep count increases by one.
- The successful rep count is prominently displayed in the top right corner.

### User Guidance

- To achieve a successful rep count, the system displays an instruction at the start: "Keep your knee bent."
- The instruction remains on the screen until the user completes 8 seconds of knee bent time.
- Once the timer hits 8 seconds, the instruction is removed, and the user can comfortably unbend their knee.

## How to Use

1. **Run the Application:**
   - Ensure your computer has a functioning camera.
   - Execute the application to initiate the Mediapipe-based Knee Bend Exercise Rep Counter.

2. **Follow On-screen Instructions:**
   - Position yourself in front of the camera.
   - Begin the knee bend exercise as instructed on the screen.

3. **Monitor Rep Count:**
   - Watch the top left corner for the timer.
   - The top right corner displays the successful rep count.

4. **Complete Reps:**
   - Maintain the knee bend for at least 8 seconds to register a successful rep count.
   - Follow the on-screen guidance to ensure accurate counting.

## Dependencies

- Python 3.x
- Mediapipe Library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/knee-bend-rep-counter.git
   cd knee-bend-rep-counter
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```
   ## Demo Video

Check out the demo video to see the Knee Bend Exercise Rep Counter in action:

https://github.com/Yaszh/Exexrcise_rep_counter/assets/71252244/bf895f58-f2bd-4091-bbd9-1e403bab7f3c

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
