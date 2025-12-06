import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_movie_data():
    base_url = "https://ssr1.scrape.center/page/{}"
    all_movies = []

    print("開始爬取電影資料...")

    for page in range(1, 11):
        url = base_url.format(page)
        print(f"正在爬取第 {page} 頁: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 尋找所有電影卡片
            items = soup.find_all(class_='el-card__body')
            
            for item in items:
                movie = {}
                
                # 電影名稱 (Title)
                title_tag = item.find('h2')
                if title_tag:
                    movie['Title'] = title_tag.get_text(strip=True)
                
                # 電影圖片 URL (Image URL)
                img_tag = item.find('img')
                if img_tag:
                    movie['Image URL'] = img_tag.get('src')
                
                # 評分 (Rating)
                score_tag = item.find(class_='score')
                if score_tag:
                    movie['Rating'] = score_tag.get_text(strip=True)
                
                # 類型 (Genre)
                # 假設類型是在 class 為 categories 的 div 下的 button 內
                cats = []
                cat_div = item.find(class_='categories')
                if cat_div:
                    for btn in cat_div.find_all('button'):
                         # 取得 span 內的文字，或者直接取得 button 文字
                         cats.append(btn.get_text(strip=True))
                
                if cats:
                    movie['Genre'] = ", ".join(cats)
                else:
                    movie['Genre'] = ""

                # 確保至少有標題才加入
                if 'Title' in movie:
                    all_movies.append(movie)

            # 隨機延遲，模擬人類行為
            time.sleep(random.uniform(0.5, 1.5))

        except Exception as e:
            print(f"爬取第 {page} 頁時發生錯誤: {e}")

    # 轉為 DataFrame
    df = pd.DataFrame(all_movies)
    
    # 簡單資料清理 (確保欄位順序)
    columns_order = ['Title', 'Image URL', 'Rating', 'Genre']
    # 如果有缺少的欄位，補上空值
    for col in columns_order:
        if col not in df.columns:
            df[col] = ""
            
    df = df[columns_order]
    
    output_file = 'movie.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig') # 使用 utf-8-sig 以便 Excel 開啟正常顯示中文
    print(f"爬取完成！共收集 {len(df)} 部電影資料。")
    print(f"檔案已儲存為: {output_file}")

if __name__ == "__main__":
    scrape_movie_data()
