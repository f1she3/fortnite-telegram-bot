# 🤖 Telegram bot for Fortnite (self hosted version)

## Intro
This project is a simple [Telegram bot](https://core.telegram.org/bots/api) aimed at [Fortnite](https://www.fortnite.com/) players.<br>
The project is built to be self hosted (raspberry pi is perfect).<br>

## Overview
Use this bot in your telegram group chat to get a regular ranking between the different members.
<br>
Feel free to fork the project, adapt it to your needs and deploy your own version of this bot to your group.

## Install
* `cd fortnite-telegram-bot`
* `docker build -t fortnite-telegram-bot .`
* Install & enable the units: 
    * Edit `units/fortnite-telegram-bot.service` and replace `<user>` in `WorkingDirectory=/home/<user>` with your username
    * `sudo cp units/fortnite-telegram-bot.service units/fortnite-telegram-bot.timer /etc/systemd/system/`
    * `sudo systemctl daemon-reload`
    * `sudo systemctl enable --now fortnite-telegram-bot.timer`

## Uninstall
* Disable the systemd timer: `sudo systemctl disable --now fortnite-telegram-bot.timer`
* Just remember to remove the systemd timer: `sudo rm /etc/systemd/system/fortnite-telegram-bot.timer /etc/systemd/system/fortnite-telegram-bot.service`

## Thanks
* The awesome [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library
* [Fortnite-API](https://fortnite-api.com/) for their service and their cool [python wrapper](https://github.com/Fortnite-API/py-wrapper)
