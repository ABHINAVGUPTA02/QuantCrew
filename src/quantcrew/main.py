from quantcrew.crew import QuantCrew
import datetime

def run():
    """
    Run the QuantCrew crew
    """
    inputs = {
        "sector": "technology",
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),   
    }
     # Create and run the crew
    result = QuantCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()