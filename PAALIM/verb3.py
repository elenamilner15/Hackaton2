import requests
from bs4 import BeautifulSoup
import psycopg2
from nltk.tokenize import RegexpTokenizer
from unicodedata import normalize

def extract_english_hebrew_words(cell): #Separation english from hebrew text
    english_span = cell.find("span", class_="dict-transcription")
    hebrew_span = cell.find("span", class_="menukad")
    
    if english_span and hebrew_span:
        english_word1 = uppercase_bold_letter(str(english_span))  # Convert the whole span, retaining <b> tags
        english_word = english_word1.get_text(strip=True)
        hebrew_word = hebrew_span.get_text(strip=True)
        return english_word, hebrew_word
    return None, None

def uppercase_bold_letter(text): #converts bold letter (stress or emphasis) to uppercase
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup.find_all('b'):
        tag.string = tag.string.upper()
    return soup 

def remove_niqqud(text):
    # Normalize the text to remove niqqud
    normalized_text = normalize('NFKD', text)
    
    # Tokenize and rejoin the text to remove punctuations
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(normalized_text)
    
    return ''.join(tokens)

conn = psycopg2.connect(
    database='mygame2',
    user='postgres',
    password='test',
    host='localhost'
)
cur = conn.cursor()

conn.commit()

base_url = "https://www.pealim.com/dict/"
page = 1
last_page = 230  # Manually set the last page value

while page <= last_page:
    url = f"{base_url}?pos=verb&num-radicals=all&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="table table-hover dict-table-t")
    rows = table.find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 4:
            english_word, hebrew_word = extract_english_hebrew_words(cells[0])
            root = cells[1].text.strip()
            part_of_speech = cells[2].text.strip()
            
            # Clean up the part_of_speech value
            part_of_speech = part_of_speech.replace("Verb –", "").replace("'", "").replace(", masculine", "").strip()
                        
            meaning = cells[3].text.strip()
            
            # Calculate the niqqud-stripped version of hebrew_word
            niqqud_stripped_word = remove_niqqud(hebrew_word)

            # Check if hebrew_word already exists in the database
            cur.execute("SELECT meaning FROM main_verbs WHERE hebrew_word = %s", (hebrew_word,))
            existing_meaning = cur.fetchone()
            if existing_meaning:
                updated_meaning = f"{existing_meaning[0]}, {meaning}"
                cur.execute(
                    "UPDATE main_verbs SET meaning = %s, part_of_speech = %s, niqqud_stripped_word = %s WHERE hebrew_word = %s",
                    (updated_meaning, part_of_speech, niqqud_stripped_word, hebrew_word)
                )
            else:
                cur.execute(
                    "INSERT INTO main_verbs (english_word, hebrew_word, root, part_of_speech, meaning, niqqud_stripped_word) VALUES (%s, %s, %s, %s, %s, %s)",
                    (english_word, hebrew_word, root, part_of_speech, meaning, niqqud_stripped_word)
                )
            
          
    conn.commit()

    print(f"Processed page {page} of {last_page}")
    page += 1

cur.close()
conn.close()