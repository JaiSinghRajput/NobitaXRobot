# NobitaXRobot
```diff
- I will not provide any support for this repo fork, so whatever happens is your responsibility. Don't contact me because of your own mistakes. I'll stop updating this repo, just a few small fixes I'll make.
```

<!--Badges-->
![MIT License][license-shield] ![Repository Size][repository-size-shield] ![Issue Closed][issue-closed-shield]

<!--Project Title Image-->
<p align="center">
   <img src="https://mallucampaign.in/images/img_1703398362.jpg"/>
</p>

<!--Project Buttons-->
  [![Readme in Indonesian][readme-ko-shield]][readme-ko-url] [![View Demo][view-demo-shield]][view-demo-url] [![Report bug][ report-bug-shield]][report-bug-url] <!-- [![Request feature][request-feature-shield]][request-feature-url] -->

<!--Table of Contents-->
# Table of Contents
- [NobitaXRobot](#nobitaxrobot)
- [Table of Contents](#table-of-contents)
- [\[1\] About Nobita](#1-about-nobita)
  - [\[2\] Framework And Server Tools Used To Build This Bot](#2-framework-and-server-tools-used-to-build-this-bot)
  - [\[3\] Donations](#3-donations)
  - [\[4\] Notes](#4-notes)
  - [\[5\] Features](#5-features)
  - [\[6\] Variables](#6-variables)
    - [Required Variables](#required-variables)
    - [Optional Variables](#optional-variables)
  - [\[7\] Deploy Tutorial (Recommended using Docker/Docker Compose)](#7-deploy-tutorial-recommended-using-dockerdocker-compose)
      - [Build And Run Using Old Methods](#build-and-run-using-old-methods)
      - [Build And Run Using Docker](#build-and-run-using-docker)
      - [Build And Run The Docker Image Using docker-compose](#build-and-run-the-docker-image-using-docker-compose)
  - [\[8\] Thanks to](#8-thanks-to)
  - [\[9\] Disclaimer](#9-disclaimer)

# [1] About Nobita
*nobita* is a Telegram Bot created using Python and the Pyrogram library. There are many useful features for us to use. I hope that one day, if this project is stopped, someone will continue or develop it again. I gave the name Nobita because I like cats, cute animals that like to play and are friendly with humans.

## [2] Framework And Server Tools Used To Build This Bot
  🌱 PyroFork v2.x.x (Pyrogram Fork with Topic, Stories and Multiple Patch Support)<br>
  🌱 Python 3.11<br>support
  🌱 MongoDB as Database<br>
  🌱 PyKeyboard for Building Pagination<br>
  🌱 VS Code<br>
  🌱 VPS/Server with Root and Docker Support (Recommended)<br>

## [3] Donations
*Indonesia Only:*<br>
  🌱 [QRIS][qris-url]<br>
  🌱 [Mayar ID][mayar]<br>

*For All Countries:*<br>
  🌱 [Paypal][paypal-url]<br>

## [4] Notes
If you want to help me fix some errors in my bot, you can create a PR to this repo. I would be very happy if you could help me. You can also provide support to me to purchase servers.

## [5] Features

| MY BOT FEATURES                                               | 🌱   |
| ------------------------------------------------------------- | --- |
| Basic Admin Features                                          | ✔️   |
| AFK Feature                                                   | ✔️   |
| Downloader FB, TikTok and YT-DLP Support                      | ✔️   |
| MultiLanguage Support (Still Beta)                            | ⚠️   |
| NightMode                                                     | ✔️   |
| ChatBot based on OpenAI, and Google Bard                      | ✔️   |
| nobita Mata                                                   | ✔️   |
| Inline Search                                                 | ✔️   |
| Sticker Tools                                                 | ✔️   |
| PasteBin Tools                                                | ✔️   |
| WebScraper (Pahe, MelongMovie, LK21, Terbit21, Kusonime, etc) | ✔️   |
| IMDB Search With Multi Language Per User                      | ✔️   |
| GenSS From Media and MediaInfo Generator                      | ✔️   |
| And Many More..                                               | ✔️   |

## [6] Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://t.me/BotFather), and get a Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `LOG_CHANNEL` : Channel to log bot activity. Make sure the bot is an admin on the channel.

### Optional Variables
* `USER_SESSION` : Session string for Userbot.
* `DATABASE_NAME`: Database name in MongoDB
* `COMMAND_HANDLER`: List of bot handler commands separated by spaces. Example: `. !` > so the bot will respond with `.cmd` or `!cmd`
* `SUDO`: User IDs that have access to the bot, separated by spaces
* `OPENAI_API`: Get from OpenAI Web
* `BARD_API`: Learn from this https://github.com/dsdanielpark/Bard-API to get cookies and set as api key.
* `CURRENCY_API`: Get API Key at https://app.exchangerate-api.com/sign-up

## [7] Deploy Tutorial (Recommended using Docker/Docker Compose)

#### Build And Run Using Old Methods
- Make sure the minimum python version is 3.8 and the maximum python 3.11 to prevent some errors. Check with this command:
```
python3 --version
```
- Install all dependencies that require the bot to run. *(requires root access, you can skip this if syour server doesn't have root access but some plugins don't work)*
```
apt update -y & apt install libjpeg-dev zlib1g-dev libwebp-dev python3-pip python3-lxml git wget curl local ffmpeg tzdata neofetch mediainfo speedtest-cli -y
```
- Install requirements.txt, if using python 3.11, you must use the venv option when installing.<br/>
*Python < 3.10*
```
pip3 install -r requirements. txt
```
*Python 3.11*
```
python3 -m venv venv_name
source nama_venv/bin/activate
pip3 install -r requirements. txt
```
- Set the config environment when running the bot and don't forget to fill in all the required values.
- Run Bot
```
bash start.sh
```

#### Build And Run Using Docker

- Start the Docker daemon (Skip if already running):
```
sudo dockerd
```
- Build Docker images:
```
sudo docker build . -t nobita
```
- Run Docker image:
```
sudo docker run nobita
```
- To Stop an image:
```
sudo docker ps
sudo docker stop <pid>
```

#### Build And Run The Docker Image Using docker-compose

- Install docker-compose
```
sudo apt install docker-compose
```
- Build and run Docker image or to view current running image:
```
sudo docker-compose up
```
- After editing files with nano for example (nano start.sh):
```
sudo docker-compose up --build
```
- To stop the running image:
```
sudo docker ps
```
```
sudo docker-compose stop <pid>
```

----


## [8] Thanks to
  - Thank Allah SWT.
  - Thanks to Dan [Pyrogram Library](https://github.com/pyrogram/pyrogram) as the base pyrofork.
  - Thanks to Mayuri [Mayuri-Chan](https://github.com/Mayuri-Chan) as the owner of the Pyrofork library.
  - Thanks to TeamDriveCok and Secret Group TBK on Telegram.
  - Thanks To [The Hamker Cat](https://github.com/TheHamkerCat) For The WilliamButcher Code.
  - Thanks to [Team Yukki](https://github.com/TeamYukki) for the AFK Bot Code.
  - Thanks To [Wrench](https://github.com/EverythingSuckz) For Some Code.
  - Thanks To [AmanoTeam](https://github.com/AmanoTeam) For MultiLanguage Template.
  - And Everyone Who Helps Me In My Life...
If your code is used in this repo and would like to give credit, please open an issue..

## [9] Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html #header)
Licensed under [GNU AGPL 2.0.](https://github.com/jaisingh007/NobitaXRobot/blob/master/LICENSE)
WARNING: *Strictly Prohibited* Selling Codes to Others for Money Without My Permission. Or I will stop this project forever...

<!--Url for Badges-->
[license-shield]: https://img.shields.io/github/license/jaisingh007/NobitaXRobot?labelColor=D8D8D8&color=04B4AE
[repository-size-shield]: https://img.shields.io/github/repo-size/jaisingh007/NobitaXRobot?labelColor=D8D8D8&color=BE81F7
[issue-closed-shield]: https://img.shields.io/github/issues-closed/jaisingh007/NobitaXRobot?labelColor=D8D8D8&color=FE9A2E

<!--Url for Buttons-->
[readme-ko-shield]: https://img.shields.io/badge/-readme%20in%20Indonesian-2E2E2E?style=for-the-badge
[view-demo-shield]: https://img.shields.io/badge/-%F0%9F%98%8E%20view%20demo-F3F781?style=for-the-badge
[view-demo-url]: https://telegram.me/Nobita_X_Robot
[report-bug-shield]: https://img.shields.io/badge/-%F0%9F%90%9E%20report%20bug-F5A9A9?style=for-the-badge
[report-bug-url]: https://github.com/jaisingh007/NobitaXRobot/issues
[request-feature-shield]: https://img.shields.io/badge/-%E2%9C%A8%20request%20feature-A9D0F5?style=for-the-badge
[request-feature-url]: https://github.com/jaisingh007/NobitaXRobot/issues

<!--URLS-->
[readme-ko-url]: README.md
[kofi-url]: https://ko-fi.com/jaisingh007
[paypal-url]: https://paypal.me/jaisingh007
[qris-url]: https://img.nobiweb.eu.org/file/2acf7698f300ef3d9138f.jpg
[mayar]: https://jaisingh007.mayar.link/payme
[sociabuzz-url]: https://sociabuzz.com/jaisingh007/tribe
[saweria-url]: https://saweria.co/jaisingh007
[trakteer-url]: https://trakteer.id/nobi-aris-sp7cn