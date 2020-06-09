# balanceApp
Ability to upload a PDF and publish a CSV to download for the same.

Install below dependency using Pip:
  - pip install Flask
  - pip install tabula-py
  - install Java to run tabula-py
  - install sql also to save the query to db
  
Working flow:
  - User Upload the pdf file and give query 
  - Flask server is made POST call with query and file content
  - *utils/pdfconverter.py* convert the PDf to CSV and save it to the upload folder
  - The same CSV file is served through an another URL.
  
Note: As our PDF will have same format and dimension we can use actual tabula to filter out the undesired part of PDF
  
 
