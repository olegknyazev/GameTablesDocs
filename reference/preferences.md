---
parent: Reference
nav_order: 5
---
# Preferences
![Game Tables Preferences UI]({{ site.baseurl }}{% link reference/preferences.png %})

Game Tables adds a *Game Tables* section to Unity's *Preferences* window (*Edit / Preferences* on Windows and Linux, *Unity / Settings* on macOS). Unlike most preferences, your sign-in isn't necessarily shared by all your projects. For details, see [Credential Storage]({{ site.baseurl }}{% link reference/google_sheets_access.md %}#credential-storage).

## Google Sheets

This section manages your Google account sign-in. Which controls are shown depends on the current state.

<a id="sign-in"></a> Sign In

: Shown when you are not signed in. Starts the sign-in flow described in [Sign In to Google Sheets]({{ site.baseurl }}{% link guides/sign_in_to_google_sheets.md %}).

<a id="cancel"></a> Cancel

: Shown while a sign-in or revoke request is in progress. Aborts the pending request.

<a id="sign-out"></a> Sign Out

: Shown when you are signed in. Deletes the credentials stored on your computer. Game Tables stays authorized in your Google account, so other computers and projects signed in with the same account are unaffected.

<a id="sign-out-and-revoke-access"></a> Sign Out and Revoke Access

: Shown when you are signed in. Deletes the credentials stored on your computer and asks Google to revoke Game Tables' access to your account. Other computers and projects signed in with the same account will need to sign in again.