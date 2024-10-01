import unittest
from knapsack_rec import initialize_knapsack  # Import the knapsack logic
class TestKnapsack(unittest.TestCase):

    def display_results(self, W, Obj, expected, actual):
        """Helper function to display and log inputs, expected, and actual outputs"""
        result = (
            f"\n--- Test Case ---\n"
            f"Knapsack Capacity (W): {W}\n"
            f"Objects (value, weight): {Obj}\n"
            f"Expected Output: {expected}\n"
            f"Actual Output: {actual}\n"
            f"------------------"
        )
        
        # Print results to console
        print(result)
        
        # Write results to file
        with open("test_results.txt", "a") as file:
            file.write(result + "\n")

    def test_knapsack_basic(self):
        W = 50
        Obj = [(60, 10), (100, 20), (120, 30)]
        expected_max_value = 220
        actual_max_value = initialize_knapsack(W, Obj)
        
        # Print and log the results
        self.display_results(W, Obj, expected_max_value, actual_max_value)
        
        # Assert to check if the test passes
        self.assertEqual(actual_max_value, expected_max_value)

    def test_knapsack_zero_capacity(self):
        W = 0
        Obj = [(60, 10), (100, 20), (120, 30)]
        expected_max_value = 0
        actual_max_value = initialize_knapsack(W, Obj)
        
        # Print and log the results
        self.display_results(W, Obj, expected_max_value, actual_max_value)
        
        self.assertEqual(actual_max_value, expected_max_value)

    def test_knapsack_single_item(self):
        W = 15
        Obj = [(30, 10)]
        expected_max_value = 30
        actual_max_value = initialize_knapsack(W, Obj)
        
        # Print and log the results
        self.display_results(W, Obj, expected_max_value, actual_max_value)
        
        self.assertEqual(actual_max_value, expected_max_value)

    def test_knapsack_no_items(self):
        W = 50
        Obj = []
        expected_max_value = 0
        actual_max_value = initialize_knapsack(W, Obj)
        
        # Print and log the results
        self.display_results(W, Obj, expected_max_value, actual_max_value)
        
        self.assertEqual(actual_max_value, expected_max_value)

if __name__ == '__main__':
    unittest.main()