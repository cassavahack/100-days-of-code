# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.

# --- Library System ---

# Books in the library
library = {
    "Dune": 3,
    "Foundation": 1
}

# Borrowed books
checked_out = []

# Checkout command
def checkout(title, borrower, due):
    if title in library and library[title] > 0:
        library[title] -= 1
        checked_out.append({
            "title": title,
            "borrower": borrower,
            "due": due
        })
        print(f"{title} checked out to {borrower}, due {due}.")
    else:
        print(f"Sorry, {title} is not available.")

# Report command
def report():
    print(f"Checked out: {len(checked_out)}")
    available_list = [f"{book}({count})" for book, count in library.items()]
    print("Available:", ", ".join(available_list))

# --- Example Run ---
checkout("Dune", "Sam", "2025-09-23")
report()