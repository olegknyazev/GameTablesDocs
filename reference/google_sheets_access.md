---
parent: Reference
nav_order: 6
---
# Google Sheets Access
Game Tables reads your spreadsheets on your behalf through the [Google Sheets API](https://developers.google.com/workspace/sheets/api) after you [sign in]({{ site.baseurl }}{% link guides/sign_in_to_google_sheets.md %}) to your Google account. For details on what data Game Tables accesses and how it's handled, see the [Game Tables Privacy Policy](https://oleg-knyazev.com/game-tables/privacy-policy/).

## Terms and Costs
Importing from Google Sheets requires a Google account. Your use of Google Sheets is subject to Google's [Terms of Service](https://policies.google.com/terms) and [Privacy Policy](https://policies.google.com/privacy).

There are no additional costs. The Google Sheets API is free to use, and you don't need a Google Cloud project or billing account of your own.

## Credential Storage
Two kinds of credentials are involved when Game Tables accesses Google Sheets:

- **Game Tables' client credentials** identify Game Tables to Google. They're part of the Game Tables Editor code, which—like the Google API libraries it uses—is Editor-only, so they're never included in your builds.
- **Your sign-in tokens** are issued by Google when you sign in. Game Tables saves them as an unencrypted JSON file in the `GameTables/AuthTokens` folder under Unity's [persistent data path](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html). This folder is in your user profile, outside your project, so the tokens are never committed to version control or included in builds. Signing out from the [Preferences]({{ site.baseurl }}{% link reference/preferences.md %}) window deletes them.

| The persistent data path depends on the **Company Name** and **Product Name** in [Player Settings](https://docs.unity3d.com/Manual/class-PlayerSettings.html), so projects with the same names share one sign-in. If you change either name, you'll need to sign in again. |
