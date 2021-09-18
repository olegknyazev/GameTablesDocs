---
parent: Reference
title: Google Sheets Authorization
nav_order: 5
---
# Authorize In Google Sheets

To use Game Tables with Google Sheets, you need to authorize in your Google account and grant Game Tables application required access. Usually it's done via Game Table object Inspector: after selecting *Google Sheets* in the [Source]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdrown your will be promted to log into your Google Account.

| It's strongly **recommended to use separate accounts** for everyone on the project who imports data from Google Sheets. If you want to have access to the same spreadsheet or folder, you may easily set it up with Google's tools. It's better than sharing the same account across all the team members. Why? Suppose someone leaves the team. How would you restrict his access to your project data? |

To login Game Table in Google perform the following steps:
1. Click the Login button.
2. Google authorization page should pop up in your default browser. Enter your Google credentials here and proceed.
3. After successful authorization you will be asked to grant access to Game Tables application. Here you will be provided with details on which application and what exactly access it will receive. Please, *check this page carefully* and only agree if you got here right from the Game Tables UI.
4. After you granted Game Tables required access, a page with *"You may now close this window"* text should appear. You may close this browser tab and switch back to Unity. Now you may continue to use Game Tables with Google Sheets.

If you switch back to Unity during authorization process, Game Tables UI tells that it waits for authorization. If you want to restart this process, press the Cancel button. This make pending authorization request outdated. If you close Game Tables UI and re-open it before completing authorization process, you have to start it from the beginning.

# Remove Authorization Data

The authentication data is saved in your personal folder on the computer. This allows you to not re-authorize each time you using Game Tables. You can remove all the authentication data from the machine if you want. To do so, open the [Preferences]({{ site.baseurl }}{% link reference/preferences.md %}) window and click Remove Authorization Data.

| Please, keep in mind that removing a file from system is not guarantee that it cannot be read by a someone. Do not share your personal computer account with anyone. If you want to be sure, that all sensitive data is removed, use specialized software or refer documentation on your operating system. |
