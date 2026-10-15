"""
Example: Scrape TikTok Shop products and sales by keyword via Apify Python Client.
Requires: pip install apify-client
"""
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQueries": ["led face mask", "wireless earbuds"],
    "countryCode": "US",
    "maxResultsPerQuery": 20,
    "sortBy": "best_seller",
    "minSold": 100
}

print("🚀 Launching TikTok Shop Search Scraper on Apify Cloud...")
run = client.actor("magic-scraper/tiktok-shop-search-scraper").call(run_input=run_input)

print(f"✅ Run finished with status: {run.get('status')}")
print("📊 Extracted Products:\n")

dataset_id = run["defaultDatasetId"]
for item in client.dataset(dataset_id).iterate_items():
    print(f"Product: {item.get('title')}")
    print(f"  Price: ${item.get('current_price')} (was ${item.get('original_price')})")
    print(f"  Sold:  {item.get('sold_count')} | Est. Revenue: ${item.get('estimated_revenue')}")
    print(f"  Store: {item.get('seller_name')} (Rating: {item.get('seller_rating')})")
    print(f"  URL:   {item.get('product_url')}\n")
