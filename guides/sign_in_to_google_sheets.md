---
parent: Guides
nav_order: 3
---
# Sign In to Google Sheets
To use Game Tables with Google Sheets, you need to sign in to your Google account and grant Game Tables read access to your spreadsheets. You can start the sign-in flow from two places:

- The [GameTable Inspector]({{ site.baseurl }}{% link reference/inspector.md %}), when *Source Type* is set to *Google Sheets*.

<p style="text-align: center;">
  <img src="{{ site.baseurl }}{% link guides/sign_in_inspector.png %}"
       alt="Sign-in prompt in the GameTable Inspector"
       width="70%">
</p>

- The [Preferences]({{ site.baseurl }}{% link reference/preferences.md %}) window.

In both places, when you are not signed in, the UI shows a *Sign In* button. Both entry points run the same flow described below.

| **Use a separate Google account for each team member who imports from Google Sheets.** Per-person sign-in lets you grant or revoke access individually without disrupting the rest of the team. |

To sign in, follow these steps:

1. Click *Sign In*.
2. Google's sign-in page opens in your default browser. Enter your Google credentials and proceed.
3. Google then asks you to grant Game Tables access to your account. The consent page lists the application and the scope it is requesting—Game Tables asks only for **read-only access to your spreadsheets**. Review the page carefully and only continue if you arrived here from Game Tables.
4. Google shows a confirmation page once access is granted. Close that browser tab and return to Unity—the *Google Sheets* section now shows that you are signed in.

If you return to Unity before completing the flow in the browser, Game Tables shows the label *Awaiting sign-in response…* along with a hint to finish signing in. To abandon the pending request, click *Cancel*.

## Sign Out

To remove the credentials stored on this computer, open the [Preferences]({{ site.baseurl }}{% link reference/preferences.md %}#sign-out) window and click *Sign Out*. After signing out, you will need to sign in again before importing from Google Sheets.

| *Sign Out* only removes the locally stored credentials. It does not revoke the access grant on Google's side. To do that, visit your [Google account permissions page](https://myaccount.google.com/permissions). |
