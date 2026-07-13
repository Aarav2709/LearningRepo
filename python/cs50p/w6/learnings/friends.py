with open("file_import/friends.csv") as file: # Importing the CSV file.
  for line in file: # Reading each line in the file.
    name, place = line.strip().split(",") # Take 2 vals.
    print(f"{name} lives in {place}!") # Export row as dict and output.
