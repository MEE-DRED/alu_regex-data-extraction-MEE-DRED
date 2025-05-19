import re
#Extract email addresses from text

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

#extract urls from text
def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

#Extract phonenumbers from text
def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

#Extract times from text
def extract_times(text):
    return re.findall(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b', text)

#Extract html tags
def extract_html_tags(text):
    return re.findall(r'<[^>]+>', text)

#Extracts hashtags
def extract_hashtags(text):
    return re.findall(r'#\w+', text)


def main():
    with open('data_sample.txt', 'r') as file:
        text = file.read()

#Call extracted functions
    print("Emails:", extract_emails(text))
    print("URLs:", extract_urls(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("Times:", extract_times(text))
    print("HTML Tags:", extract_html_tags(text))
    print("Hashtags:", extract_hashtags(text))

if __name__ == "__main__":
    main()
