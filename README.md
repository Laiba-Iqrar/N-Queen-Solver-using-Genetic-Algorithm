# Visualized-N-Queen-Solver-Using-GA
Visualization of N Queen Problem using Genetic Algorithm and Tkinter

## Features
- Solves the N-Queens problem for `N ≥ 4`.
- Uses a genetic algorithm to find solutions.
- Displays solutions on a graphical chessboard.

## Requirements
- Python 3.8+
- Libraries:
  - `tkinter` (built-in)
  - `random` (built-in)

## Directory Structure
```

├── main.py            
├── n_queen_solver.py 
└── n_queen_ui.py      
```

## How to Run
1. Clone the repository.
2. Run `main.py`:
   ```bash
   python main.py
   ```

## Key Components
### Genetic Algorithm (in `n_queen_solver.py`)
- **Initial Population:** Randomly generates potential solutions.
- **Fitness Function:** Measures the number of non-attacking pairs of queens.
- **Selection:** Chooses the top-performing chromosomes.
- **Crossover:** Combines parent chromosomes to create offspring.
- **Mutation:** Introduces variability by swapping positions of queens.

### GUI (in `n_queen_ui.py`)
- Input: Accepts the value of `N`.
- Visualization: Displays solutions on a chessboard.
- Navigation: "Next Solution" button cycles through solutions.

## Constraints
- `N ≥ 4` (No solutions exist for smaller values). 


