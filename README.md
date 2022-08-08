#BROWSER USAGE#

https://paste.rs/web

#API USAGE#
`POST https://paste.rs/`

Send the raw data along. Will respond with a link to the paste.

- **Response code 201 (Created)**
The entire paste was uploaded.
- **Response code 206 (Partial)**
The paste exceeded the maximum upload size, only part of the paste was uploaded.
- **Other response codes**
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

#Examples#

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