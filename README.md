# Pastebin-Telegram 📺

Open-Bot for Telegram


[![GitHub issues](https://img.shields.io/github/issues/Mr-Sunglasses/pastebin-telegram)](https://github.com/Mr-Sunglasses/pastebin-telegram/issues)
[![GitHub forks](https://img.shields.io/github/forks/Mr-Sunglasses/pastebin-telegram)](https://github.com/Mr-Sunglasses/pastebin-telegram/network)
[![GitHub stars](https://img.shields.io/github/stars/Mr-Sunglasses/pastebin-telegram)](https://github.com/Mr-Sunglasses/pastebin-telegram/stargazers)
[![GitHub license](https://img.shields.io/github/license/Mr-Sunglasses/pastebin-telegram)](https://github.com/Mr-Sunglasses/pastebin-telegram/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/Mr-Sunglasses/pastebin-telegram) 
<br>





### BROWSER USAGE

https://paste.rs/web

### API USAGE
`POST https://paste.rs/`

Send the raw data along. Will respond with a link to the paste.

- **Response code 201 (Created):**
The entire paste was uploaded.
- **Response code 206 (Partial):**
The paste exceeded the maximum upload size, only part of the paste was uploaded.
- **Other response codes:**
An error occurred.

Pasting is heavily rate limited.

---
`GET https://paste.rs/<id>`

Retrieve the paste with the given id as plain-text.

---

`GET https://paste.rs/<id>.<ext>`

Retrieve the paste with the given id. If ext is a known code file extension, the paste is syntax highlighted and returned as HTML. If ext is a known file extension, the paste is returned with the extension's corresponding Content-Type. Otherwise, the paste is returned as plain text.

---

`DELETE https://paste.rs/<id>`

Delete the paste with the given id.

### Examples

- **Paste a file named 'file.txt' using PowerShell:**

`Invoke-RestMethod -Uri "https://paste.rs" -Method Post -InFile .\file.txt`

- **Paste from stdin using PowerShell:**

`echo "Hi!" | Invoke-RestMethod -Uri "https://paste.rs" -Method Post`

- **Delete an existing paste with id <id> using PowerShell:**

`Invoke-RestMethod -Uri "https://paste.rs/<id>" -Method Delete`

- **A PowerShell function that can be used for quick pasting from the command line. The command takes a filename or reads from stdin if none was supplied and outputs the URL of the paste to stdout: 'Paste file.txt' or 'echo hi" | Paste'.**

```
function Paste([string]$file) {
              $Data = if ($file) {Get-Content $file} else {$input}
              Invoke-RestMethod -Uri "https://paste.rs" -Method Post -Body $Data
          }
```

Run Through Docker

docker build -t container_name .

docker run -e TOKEN=TELEGRAM_BOT_TOKEN -e username=INTA_USER-NAME -e password=INSTA_PASSWORD container_name:latest

## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping AutoType grow.   
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=Mr-Sunglasses/pastebin-telegram)](https://github.com/Mr-Sunglasses/pastebin-telegram/graphs/contributors)

## 🙏 Support++

This project needs your shiny star ⭐.   
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

