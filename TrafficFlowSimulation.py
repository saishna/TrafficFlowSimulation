import matplotlib.pyplot as plt
import numpy as np
import random

class TrafficSimulation:
    def __init__(self, road_length=100, num_vehicles=30, max_speed=5, prob_slowdown=0.2):
        self.road_length = road_length
        self.num_vehicles = num_vehicles
        self.max_speed = max_speed
        self.prob_slowdown = prob_slowdown

        # Initialize random positions and speeds for vehicles
        self.positions = np.sort(np.random.choice(range(self.road_length), self.num_vehicles, replace=False))
        self.speeds = np.random.randint(1, self.max_speed + 1, size=self.num_vehicles)

    def update(self):
        for i in range(self.num_vehicles):
            # Acceleration
            if self.speeds[i] < self.max_speed:
                self.speeds[i] += 1

            # Slowdown due to other vehicles
            for j in range(1, self.speeds[i] + 1):
                if (self.positions[i] + j) % self.road_length in self.positions:
                    self.speeds[i] = j - 1
                    break

            # Random slowdown
            if random.random() < self.prob_slowdown and self.speeds[i] > 0:
                self.speeds[i] -= 1

        # Update positions based on speeds
        self.positions = (self.positions + self.speeds) % self.road_length

    def plot(self):
        road = [' '] * self.road_length
        for i in range(self.num_vehicles):
            road[self.positions[i]] = str(self.speeds[i])

        print(''.join(road))

    def simulate(self, num_steps=50):
        for _ in range(num_steps):
            self.update()
            self.plot()
            print('-' * self.road_length)

if __name__ == "__main__":
    simulation = TrafficSimulation(road_length=30, num_vehicles=10, max_speed=5, prob_slowdown=0.1)
    simulation.simulate(num_steps=20)
