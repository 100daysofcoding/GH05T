import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def brute_force_directory(url, directory, wordlist):
    full_url = f"{url}/{directory}"
    
    with open(wordlist, 'r') as f:
        wordlist_lines = f.readlines()
        total_combinations = len(wordlist_lines)
        
        for line in tqdm(wordlist_lines, total=total_combinations, desc=f"Testing {full_url}"):
            word = line.strip()
            test_url = f"{full_url}/{word}"
            response = requests.get(test_url, allow_redirects=False)
            
            if response.status_code == 200:
                print(f"Directory found: {test_url}")

def main():
    target_url = input("Enter the target URL: ")
    target_directory = input("Enter the target directory (e.g., /admin): ")
    wordlist_path = input("Enter the path to the wordlist file: ")

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(brute_force_directory, target_url, target_directory, wordlist_path)

if __name__ == "__main__":
    main()
