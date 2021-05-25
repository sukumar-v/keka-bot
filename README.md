# Keka Bot

A simple bot to clock in and out of Keka. Made using Selenium.

# Getting Started

1. Install firefox browser
2. Install geckodriver
3. Install python dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Rename `.env_sample` to `.env` and edit your login & location settings
   ```bash
   cp .env_sample .env
   ```
5. Rename `configs/config_sample.py` to `configs/config.py` and edit the options to your heart's content
   ```bash
   cp configs/config_sample.py configs/config.py
   ```


# Usage

### Clock in
```python
python start_keka_bot.py --clock_in
```

### Clock out
```python
python start_keka_bot.py --clock_out
```

# Additional Arguments

- Headless mode<br>
  `-hl`, `--headless` - use headless browser mode