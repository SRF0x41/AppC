#!/usr/bin/python3
import sys,csv,os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATA_BASE_PATH = os.getenv('DB_PATH')
CSV_MAIN = os.getenv('CSV_PATH')

csv_path = DATA_BASE_PATH + "/" + CSV_MAIN

def count_rows_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Count the rows by iterating over the reader
        row_count = sum(1 for row in reader)
    return row_count

def main():
    if len(sys.argv) == 1:
        print("No arguments passed. Input a website")
        sys.exit(0)
        
    app_url = sys.argv[1]
    
    with open(csv_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([app_url])  # Append a single row
    print("Number of applications:", count_rows_csv(csv_path))
    


if __name__ == "__main__":
    main()
