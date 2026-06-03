import pandas as pd

# Load dataset
df = pd.read_csv("books.csv")

print("--------------------------")
print("BOOK RECOMMENDATION SYSTEM")
print("--------------------------")


while True:
    print("\nAvailable Genres:")
    genres = sorted(df['Genre'].unique())

    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    try:
        choice = int(input("\nSelect Genre Number: "))

        if choice < 1 or choice > len(genres):
            print("Invalid Choice!")
            continue

        selected_genre = genres[choice - 1]

        recommendations = df[df['Genre'] == selected_genre]

        recommendations = recommendations.sort_values(
            by='Rating',
            ascending=False
        )

        print("\nRecommended Books")
        print("-"*60)

        for _, row in recommendations.iterrows():
            print(
                f" {row['Title']} | "
                f"Author: {row['Author']} | "
                f"Rating: {row['Rating']}"
            )

    except ValueError:
        print("Please enter a valid number.")
        continue

    again = input("\nDo you want more recommendations? (y/n): ")

    if again.lower() != 'y':
        print("\nThank you for using the Book Recommendation System!")
        break