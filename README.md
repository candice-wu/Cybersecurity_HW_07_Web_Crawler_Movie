# 電影網站爬蟲專案 (Movie Crawler Project)

本文件依據 CRISP-DM (Cross-Industry Standard Process for Data Mining) 流程架構撰寫，說明本專案之開發與執行細節。

## 1. 商業理解 (Business Understanding)
- **專案背景**: 針對指定電影網站 [Scrape | Movie](https://ssr1.scrape.center/) 進行資料蒐集之作業需求。
- **商業目標**: 自動化爬取網站上 10 頁的電影資料，以利後續資料分析或應用。
- **需求**:
    - 爬取 1 到 10 頁的每一部電影資訊。
    - 欄位包含：電影名稱、圖片 URL、評分、類型。
    - 產出格式：CSV 檔案 (`movie.csv`)。

## 2. 資料理解 (Data Understanding)
- **資料來源**: [https://ssr1.scrape.center/](https://ssr1.scrape.center/)
- **資料特性**:
    - **結構**: HTML 網頁，列表式呈現。
    - **分頁**: 透過 URL `/page/{number}` 進行分頁，共 10 頁。
    - **目標欄位**:
        - Title (`h2` 標籤)
        - Image URL (`img` 標籤 src)
        - Rating (評分區塊文字)
        - Genre (類別按鈕文字)

## 3. 資料準備 (Data Preparation)
本階段為專案核心，即「爬蟲程式開發」。
- **使用技術**: Python, Requests, BeautifulSoup, Pandas。
- **資料清理**:
    - 處理缺漏值 (若無評分或類型則留空)。
    - 去除多餘空白 (`strip=True`)。
    - 格式化輸出為標準 CSV (UTF-8-SIG 編碼)。

## 4. 建模 (Modeling)
*(本專案為資料蒐集性質，不涉及機器學習建模，故此階段著重於「資料獲取邏輯」)*
- **實作邏輯**:
    1. 定義基礎 URL 樣板。
    2. 迴圈遍歷頁碼 1 至 10。
    3. 發送 HTTP GET 請求。
    4. 解析 HTML DOM Tree。
    5. 提取目標欄位並存入 List。
    6. 加入隨機延遲 (Random Delay) 避免對伺服器造成過大負擔。

## 5. 評估 (Evaluation)
- **測試結果**:
    - 成功爬取 10 頁，共 **100 筆** 電影資料。
    - `movie.csv` 欄位完整，無亂碼情形。
    - 圖片連結均為有效路徑。

## 6. 部署 (Deployment)
### 專案結構
```
Security/HW7/
├── movie_crawler.py  # 主要爬蟲程式
├── movie.csv         # 爬取結果
├── requirements.txt  # (可選) 依賴套件
├── README.md         # 專案說明文件
├── prompt/           # 對話記錄
└── venv/             # 虛擬環境 (Git Ignored)
```

### 如何執行
1. **建立虛擬環境 (建議)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

2. **安裝依賴套件**:
   ```bash
   pip install requests pandas beautifulsoup4
   ```

3. **執行爬蟲**:
   ```bash
   python movie_crawler.py
   ```
   程式執行完畢後，將於同目錄下產生 `movie.csv`。

---
**Author**: Antigravity & User
**Date**: 2025/12/07
