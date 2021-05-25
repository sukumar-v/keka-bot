# Keka Bot

A simple bot to clock in and out of Keka, an attendence management system. Powered by Selenium.

## Getting Started

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


## Usage

### Clock in
```python
python start_keka_bot.py --clock_in
```

### Clock out
```python
python start_keka_bot.py --clock_out
```

## Additional Arguments

- Headless mode<br>
  `-hl`, `--headless` - use headless browser mode

## Run as CRON job

1. open crontab config
   ```bash
   crontab -e
   ```
2. Add the following lines at the bottom of the file
   ```bash
   0 9 * * 1-5 path/to/bin/python path/to/start_keka_bot.py --clock_in --silent --headless
   0 19 * * 1-5 path/to/bin/python path/to/start_keka_bot.py --clock_out --silent --headless
   ```
   The first job will start at 9 AM in the morning every day of the week from Monday to Friday. Whereas the second job will start at 7 PM in the evening every day of the week from Monday to Friday.<br>
   Please refer to [crontab(5)](https://man7.org/linux/man-pages/man5/crontab.5.html) and [crontab.guru](https://crontab.guru/#0_9_*_*_1-5) for more details on configuring CRON jobs<br>

   **Note:** A random delay can be set by editing the value of `max_delay` in `configs/config.py`. This will ensure that the bots starts at a different time everyday.