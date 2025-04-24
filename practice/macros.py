import pandas as pd
import os
from datetime import datetime

class DailyMacroTracker:
    def __init__(self, calory_goal=2500, protein_goal=200, fat_goal=66, carb_goal=280, state_file="current_day.csv", meals_file="meals.csv"):
        self.calory_goal = calory_goal
        self.protein_goal = protein_goal
        self.fat_goal = fat_goal
        self.carb_goal = carb_goal
        self.state_file = state_file
        self.meals_file = meals_file
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Initialize predefined meals by loading from the meals file
        self.predefined_meals = self._load_predefined_meals()

        # Load previous state if the state file exists
        if os.path.exists(self.state_file) and os.path.getsize(self.state_file) > 0:
            state = pd.read_csv(self.state_file)
            if state.loc[0, "Date"] == self.current_date:
                # Continue from the last saved state for today
                self.daily_calories = state.loc[0, "Remaining Calories"]
                self.daily_protein = state.loc[0, "Remaining Protein"]
                self.daily_fat = state.loc[0, "Remaining Fat"]
                self.daily_carbs = state.loc[0, "Remaining Carbs"]
            else:
                # Reset for a new day
                self._reset_daily_macros()
        else:
            # No previous state, start fresh
            self._reset_daily_macros()

    def _reset_daily_macros(self):
        self.daily_calories = self.calory_goal
        self.daily_protein = self.protein_goal
        self.daily_fat = self.fat_goal
        self.daily_carbs = self.carb_goal

    def _save_current_state(self):
        state = pd.DataFrame([{
            "Date": self.current_date,
            "Remaining Calories": self.daily_calories,
            "Remaining Protein": self.daily_protein,
            "Remaining Fat": self.daily_fat,
            "Remaining Carbs": self.daily_carbs
        }])
        state.to_csv(self.state_file, index=False)
    
    def _load_predefined_meals(self):
        if os.path.exists(self.meals_file) and os.path.getsize(self.meals_file) > 0:
            return pd.read_csv(self.meals_file).set_index("Meal").to_dict("index")
        else:
            return {}

    def _save_predefined_meals(self):
        if self.predefined_meals:
            df = pd.DataFrame.from_dict(self.predefined_meals, orient="index").reset_index()
            df.columns = ["Meal", "Fat", "Carbs", "Protein"]
            df.to_csv(self.meals_file, index=False)

    def enter_meal(self, fat, carbs, protein):
        calories = fat * 9 + carbs * 4 + protein * 4
        self.daily_calories -= calories
        self.daily_protein -= protein
        self.daily_fat -= fat
        self.daily_carbs -= carbs
        print(f"Remaining - Calories: {self.daily_calories}, Protein: {self.daily_protein}, Fat: {self.daily_fat}, Carbs: {self.daily_carbs}")
        self._save_current_state()

    def enter_predefined_meal(self, meal_name):
        if meal_name in self.predefined_meals:
            meal = self.predefined_meals[meal_name]
            self.enter_meal(meal["Fat"], meal["Carbs"], meal["Protein"])
        else:
            print(f"Meal '{meal_name}' not found in predefined meals.")

    def add_new_meal(self, meal_name, fat, carbs, protein):
        self.predefined_meals[meal_name] = {"Fat": fat, "Carbs": carbs, "Protein": protein}
        self._save_predefined_meals()
        print(f"Meal '{meal_name}' added to predefined meals.")
        self.enter_meal(fat, carbs, protein)

    def close_day(self, file_name="daily_macros.csv"):
        # Calculate total consumed macros
        consumed_calories = self.calory_goal - self.daily_calories
        consumed_protein = self.protein_goal - self.daily_protein
        consumed_fat = self.fat_goal - self.daily_fat
        consumed_carbs = self.carb_goal - self.daily_carbs

        # Create a record for the day
        day_record = {
            "Date": self.current_date,
            "Calories Consumed": consumed_calories,
            "Protein Consumed": consumed_protein,
            "Fat Consumed": consumed_fat,
            "Carbs Consumed": consumed_carbs
        }

        # Check if the file exists and is not empty
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            df = pd.read_csv(file_name)
            df = pd.concat([df, pd.DataFrame([day_record])], ignore_index=True)
        else:
            # Create a new DataFrame if the file does not exist or is empty
            df = pd.DataFrame([day_record])

        # Save the updated DataFrame to the CSV file
        df.to_csv(file_name, index=False)
        print(f"Day closed. Data saved to {file_name}.")

        # Reset for the next day and delete the state file
        self._reset_daily_macros()
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

if __name__ == "__main__":
    tracker = DailyMacroTracker()

    while True:
        print("\nOptions:")
        print("1. Enter a new meal")
        print("2. Enter a predefined meal")
        print("3. Enter macros directly (without saving as a meal)")
        print("4. Close the day")
        print("5. Exit without saving")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            try:
                meal_name = input("Enter the name of the new meal: ").lower()
                fat = int(input("Enter fat (g): "))
                carbs = int(input("Enter carbs (g): "))
                protein = int(input("Enter protein (g): "))
                tracker.add_new_meal(meal_name, fat, carbs, protein)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            meal_name = input("Enter the name of the predefined meal: ").lower()
            tracker.enter_predefined_meal(meal_name)
        elif choice == "3":
            try:
                fat = float(input("Enter fat (g): "))
                carbs = float(input("Enter carbs (g): "))
                protein = float(input("Enter protein (g): "))
                tracker.enter_meal(fat, carbs, protein)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "4":
            tracker.close_day()
            break
        elif choice == "5":
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")