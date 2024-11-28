import random

class NQueenSolver:
    def __init__(self, N):
        self.N = N
        self.population_size = 100
        self.mutation_rate = 0.1
        self.generations = 5000
        self.population = self.generate_initial_population()
        self.solutions = []
        self.find_all_solutions()

    def generate_initial_population(self):
        return [random.sample(range(self.N), self.N) for _ in range(self.population_size)]

    def fitness(self, chromosome):
        non_attacking = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if abs(chromosome[i] - chromosome[j]) != abs(i - j):  # Check diagonal attack
                    non_attacking += 1
        return non_attacking

    def selection(self):
        weighted_population = [(self.fitness(ch), ch) for ch in self.population]
        weighted_population.sort(reverse=True, key=lambda x: x[0])
        return [ch for _, ch in weighted_population[:self.population_size // 2]]

    def crossover(self, parent1, parent2):
        split = random.randint(1, self.N - 2)
        child = parent1[:split] + [g for g in parent2 if g not in parent1[:split]]
        return child

    def mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.N), 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

    def evolve(self):
        new_population = []
        selected = self.selection()
        for _ in range(self.population_size):
            parent1, parent2 = random.sample(selected, 2)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            new_population.append(child)
        self.population = new_population

    def find_all_solutions(self):
        seen = set()
        for _ in range(self.generations):
            for chromosome in self.population:
                if self.fitness(chromosome) == self.N * (self.N - 1) // 2:  # Max fitness
                    solution = tuple(chromosome)
                    if solution not in seen:
                        self.solutions.append(solution)
                        seen.add(solution)
            self.evolve()
