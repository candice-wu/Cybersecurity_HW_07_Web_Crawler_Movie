# 實作計畫 (Implementation Plan)

## 目標
開發一個 Python 爬蟲程式，從 [https://ssr1.scrape.center/](https://ssr1.scrape.center/) 爬取 10 頁電影資料，並將結果儲存為 CSV 檔案。

## 使用工具與函式庫
- Python 3
- `requests`: 用於發送 HTTP 請求取得網頁內容。
- `beautifulsoup4` (bs4): 用於解析 HTML 並提取所需資料。
- `pandas`: 用於整理資料並輸出為 CSV (或者直接使用 Python內建 `csv` 模組，但 pandas 處理結構化資料更方便，這裡預計使用 pandas)。

## 預計變更與檔案結構

### [NEW] `movie_crawler.py`
這是主要的爬蟲程式碼。
- **流程邏輯**:
    1. 定義基礎 URL 格式: `https://ssr1.scrape.center/page/{page_number}`
    2. 使用迴圈遍歷頁碼 1 到 10。
    3. 對每一頁發送 GET 請求。
    4. 檢查回應狀態碼 (200 OK)。
    5. 使用 BeautifulSoup 解析 HTML。
    6. 選取電影列表項目 (card/item)。
    7. 針對每個項目提取：
        - **電影名稱 (Title)**: 透過 `h2` 標籤提取。
        - **電影圖片 URL (Image URL)**: 透過 `img` 標籤的 `src` 屬性提取 (需注意可能是封面圖)。
        - **評分 (Rating)**: 提取評分區塊文字。
        - **類型 (Genre/Categories)**: 提取標籤/分類按鈕的文字，並以逗號分隔組合。
    8. 將資料暫存於 List of Dictionaries。
    9. 所有頁面爬取完成後，轉換為 DataFrame 並存為 `movie.csv`。

### [NEW] `movie.csv`
- 程式執行後的產出檔案，包含欄位：`Title`, `Image URL`, `Rating`, `Genre`。

### [NEW] `README.md`
- 使用 CRISP-DM 架構撰寫的文件，說明專案背景、資料理解、資料準備 (爬蟲)、建模 (此處為資料收集)、評估與佈署 (執行方式)。

## 驗證計畫
### 自動化測試 / 執行驗證
1. **單頁測試**: 先嘗試爬取第 1 頁，列印出提取的資料，確認欄位正確且無缺漏。
2. **完整執行**: 執行 `python movie_crawler.py`，確認程式能跑完 10 頁且不中斷。
3. **資料檢查**: 打開 `movie.csv`，檢查：
    - 是否有 100 筆資料 (假設每頁 10 筆 x 10 頁)。
    - 檢查是否有亂碼或空值。
    - 檢查圖片連結是否有效 (隨機抽樣)。
