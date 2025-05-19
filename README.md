This is a README.md file for Regular expressions.


It is a python-based project designed to extract structured data from unstructured text using Regular Expressions (regex). In this task, I implemented 6 form field validations: Email, URL, phone number, times, Html tags and hashtags.




My tree folder, Regex Hackathon, houses a regex_extractor.py file that contains all regex extraction functions, a Test folder and a test file that contains all unittest for the extraction functions, and a data_samples.txt file that contains all sample datat used for extraction.



├── Regex Hackathon


├── test


├── data_samples.txt


├── regex_extractor.py


This project supports the extraction of emails, URLs, phone numbers, times, Html tags, and hashtags in standard formats.


To run the file,


The root directory should be set to Regex Hackathon


cd Regex Hackathon


Then the command python .\regex_extractor.py displays the files in the data_sample.txt file.


This interpretes as;


Emails: ['user@example.com', 'firstname.lastname@company.co.uk', 'm.ebomah@alustudent.com']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Times: ['17:30', '19:30 PM']
HTML Tags: ['<p>', '<div class="example">', '<img src="image.jpg" alt="description">']
Hashtags: ['#example', '#ThisIsAHashtag']


