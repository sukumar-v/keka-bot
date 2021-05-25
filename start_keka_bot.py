import argparse
import random
import time

from configs.config import config
from src.keka_bot import KekaBot


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-in", "--clock_in", help="clock in of keka", default=False, action="store_true"
    )
    group.add_argument(
        "-o",
        "--clock_out",
        help="clock out of keka",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-hl",
        "--headless",
        help="use headless browser mode",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-s", "--silent", help="Dont print any text", default=False, action="store_true"
    )
    args = parser.parse_args()

    # Set argparse configs
    config["run"]["headless"] = args.headless
    config["run"]["silent"] = args.silent

    seconds_to_delay = random.randint(0, config["run"]["delay"])

    if not config["run"]["silent"]:
        print(f"starting in {seconds_to_delay} seconds...")

    time.sleep(seconds_to_delay)

    if not config["run"]["silent"]:
        print("Bot started!")

    bot = KekaBot(config)

    # Login to Keka
    bot.login()

    if args.clock_in:
        # Clock into Keka
        bot.clock_in()
    elif args.clock_out:
        # Clock out of Keka
        bot.clock_out()

    # close session
    bot.close()
