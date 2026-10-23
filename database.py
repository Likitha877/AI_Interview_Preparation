import csv
import os

FILE_NAME = "results.csv"


def save_result(name, interview, score, total):

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name",
                "Interview",
                "Score",
                "Total"
            ])

        writer.writerow([
            name,
            interview,
            score,
            total
        ])