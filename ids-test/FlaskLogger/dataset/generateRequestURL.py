import random
import string

# Define the base URL
base_url = "http://127.0.0.1:5000/"

# Define a list of finance-related words
finance_words = ["account", "transaction", "balance", "deposit", "withdrawal", "loan", "credit", "debit", "mortgage", "interest","stock", "portfolio", "invest", "dividend", "capital", "market", "equity", "fund", "loan", "credit", "interest"]

# Define the number of URIs to generate
num_uris = 10000

# Generate the URIs
uris = []
for i in range(num_uris):
    # Choose a finance-related word at random
    word = random.choice(finance_words)
    
    # Generate a random string of letters and digits
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    
    # Combine the base URL, finance-related word, and random string to form the URI
    uri = f"{base_url}{word}/{random_string}"
    
    # Add the URI to the list
    uris.append(uri)

# Write the URIs to a file
with open('finance_uris.txt', mode='w') as file:
    for uri in uris:
        file.write(uri + '\n')

print(f"Successfully generated {num_uris} URIs and wrote them to finance_uris.txt.")
