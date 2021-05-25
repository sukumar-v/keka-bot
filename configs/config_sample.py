config = {
    "setup": {
        "geckodriver_path": "/usr/local/bin/geckodriver"  # Path to geckodriver executable
    },
    "run": {
        "headless": False,  # Run the bot in headless browser mode
        "silent": False,  # Will print debug messages if True
        "max_delay": 3600  # Maximum time delay in seconds. A random delay between 0 & max_delay will be enforced before starting the bot.
    },
    "urls": {
        "keka_attendance": "https://<SUB_DOMAIN_NAME>.keka.com/ui/#/me/attendance/logs"  # Keka attendence URL
    },
    "xpaths": {
        "keka_login_type_botton": "/html/body/div[3]/table/tbody/tr/td/div/div/div[3]/form/button[1]",
        "sign_in_email_input": '//*[@id="i0116"]',
        "sign_in_password_input": '//*[@id="i0118"]',
        "stay_signed_in_botton": '//*[@id="idSIButton9"]',
        "web_clock_in_button": "/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/a[1]",
        "web_clock_out_button": "/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/div[1]/button",
        "clock_out_confirmation_button": "/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/div[1]/button[1]",
    }
}
