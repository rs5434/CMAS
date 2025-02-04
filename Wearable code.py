#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random
from datetime import datetime

# Simulated Classes for Wearable Device, Mobile App, and Analytics

class WearableDevice:
    def __init__(self):
        self.sleep_data = []  # Sleep hours per night
        self.activity_data = []  # Steps per day
        self.heart_rate = []  # Average daily heart rate

    def collect_data(self):
        # Simulate data collection
        self.sleep_data.append(random.uniform(4, 9))
        self.activity_data.append(random.randint(2000, 10000))
        self.heart_rate.append(random.randint(60, 100))
        return {
            "sleep": self.sleep_data[-1],
            "activity": self.activity_data[-1],
            "heart_rate": self.heart_rate[-1]
        }

class CognitiveTests:
    def __init__(self):
        self.memory_scores = []  # Scored out of 10
        self.reaction_times = []  # Measured in milliseconds

    def run_memory_test(self):
        score = random.randint(5, 10)
        self.memory_scores.append(score)
        return score

    def run_reaction_time_test(self):
        reaction_time = random.randint(200, 500)
        self.reaction_times.append(reaction_time)
        return reaction_time

class Analytics:
    @staticmethod
    def detect_anomalies(data):
        thresholds = {
            "sleep": (5, 8),
            "activity": (3000, 8000),
            "heart_rate": (60, 90),
            "memory": 7,
            "reaction_time": 400
        }

        anomalies = {}
        for key, value in data.items():
            if key in thresholds:
                if isinstance(thresholds[key], tuple):
                    if not (thresholds[key][0] <= value <= thresholds[key][1]):
                        anomalies[key] = value
                else:
                    if key == "memory" and value < thresholds[key]:
                        anomalies[key] = value
                    elif key == "reaction_time" and value > thresholds[key]:
                        anomalies[key] = value
        return anomalies

# Main System Simulation

def run_monitoring_system():
    wearable = WearableDevice()
    cognitive_tests = CognitiveTests()

    while True:
        print("\nCollecting data...\n")

        # Collect data from wearable
        wearable_data = wearable.collect_data()

        # Run cognitive tests
        memory_score = cognitive_tests.run_memory_test()
        reaction_time = cognitive_tests.run_reaction_time_test()

        # Aggregate data
        collected_data = wearable_data
        collected_data.update({
            "memory": memory_score,
            "reaction_time": reaction_time
        })

        # Analyze data for anomalies
        anomalies = Analytics.detect_anomalies(collected_data)

        # Print Results
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Collected Data: {collected_data}")
        if anomalies:
            print("\nAnomalies Detected:")
            for key, value in anomalies.items():
                print(f" - {key.capitalize()}: {value}")
        else:
            print("\nNo anomalies detected. All metrics are within thresholds.")

        # Wait for the next collection cycle (e.g., 24 hours in real use)
        time.sleep(5)  # Simulate short delay for testing purposes

# Run the system simulation
if __name__ == "__main__":
    try:
        run_monitoring_system()
    except KeyboardInterrupt:
        print("\nMonitoring system terminated.")


# In[ ]:




