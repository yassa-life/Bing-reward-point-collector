
# Bing Rewards Automation Script

A Python script that automates Bing searches to help earn Microsoft Rewards points.

## Features

- 🚀 Automated Bing searches with random queries  
- ⏱️ Human-like random delays between searches  
- 🌐 Uses Firefox browser (configurable)  
- 📊 Diverse search terms to appear more natural  
- 🔒 Graceful error handling and interrupt support  

## Prerequisites

- Python 3.7+
- Firefox browser installed (or modify for your preferred browser)
- Required Python packages: **None** (uses built-in libraries)

## Installation

1. Clone the repository:

   git clone https://github.com/yassa-life/Bing-reward-point-collector.git
   cd Bing-reward-point-collector

2. Verify Firefox is installed at the default location or edit the path in the script:

   ```python
   FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
   ```

## Usage

Run the script:

```bash

The script will:

1. Open Firefox
2. Perform 40 random searches
3. Wait random intervals between searches (5–20 seconds normally, occasionally longer)

To stop the script early, press `Ctrl+C`.

## Customization

### Modify Search Queries

Edit the `SEARCH_QUERIES` list in the script to add/remove search terms.

### Change Browser

To use a different browser:

1. Update the path in `FIREFOX_PATH`
2. Or replace with:

   ```python
   # For Chrome:
   webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
   webbrowser.get('chrome').open(url)
   ```

### Adjust Timing

Modify these values:

```python
# Normal delay range (seconds)
random_delay(5, 20)

# Occasional longer delay (30–60 seconds)
if random.random() < 0.1:
    time.sleep(random_delay(30, 60))
```

## Disclaimer

⚠️ This script is for educational purposes only. Microsoft's terms of service may prohibit automated searches. Use at your own discretion.
