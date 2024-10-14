import pandas as pd
import os
import requests


df = pd.read_excel('FEED.xlsx')  
print(df.head())  


def download_image(url, number, index=None):
    try:
    
        response = requests.get(url)
        if response.status_code == 200:
        
            # Enforce the filename to use .jpg format
            if index is None:
                filename = f"{number}.jpg"
            else:
                filename = f"{number}-{index}.jpg"

            save_dir = 'images'
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            with open(os.path.join(save_dir, filename), 'wb') as f:
                f.write(response.content)

            print(f"Downloaded and saved: {filename}")
        else:
            print(f"Failed to download image from {url}")

    except Exception as e:
        print(f"Error downloading image from {url}: {e}")


for index, row in df.iterrows():
    number = row['Number']  
    
   
    for i in range(11):  
        link_column = f'Link{i}' if i > 0 else 'Link'  
        link = row.get(link_column)  

        if pd.notnull(link): 
            download_image(link, number, None if i == 0 else i)
        else:
            print(f"No link found for number {number} in column {link_column}")

print("Image download process completed.")
