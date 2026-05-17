---
parent: Guides
nav_order: 2
---
# Import from Google Sheets
To set up importing from Google Sheets, follow these steps:
1. Create a GameTable object (right-click in the Project window and choose *Create / Game Tables / Game Table*).
2. Set up the GameTable object properties:
    1. Choose *Google Sheets* in the [Source Type]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdown. If you aren't signed in to Google yet, sign in first. See [Sign In to Google Sheets]({{ site.baseurl }}{% link guides/sign_in_to_google_sheets.md %}) for details.
    2. Paste the spreadsheet's URL—or just its ID—into the [Spreadsheet Id]({{ site.baseurl }}{% link reference/inspector.md %}#spreadsheet-id) field.
    3. Game Tables supports only documents in the US locale (en_US). If the document uses a different locale, change it from the *File / Spreadsheet Settings* menu in Google Sheets.
    4. In the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) field, enter the path to the folder containing the Prefabs the spreadsheet references. The path is relative to the project root, for example *Assets/Prefabs/Units*.
    5. Optional. Specify additional settings that alter the way the table data should be interpreted. For example, you can choose whether to use object-per-row or property-per-row orientation. For more, see [GameTable Inspector]({{ site.baseurl }}{% link reference/inspector.md %}).
3. Click [Apply Game Table]({{ site.baseurl }}{% link reference/inspector.md %}#apply-game-table).
4. Check the Console window. If everything went well, it should contain a message like the following:
   > Game Tables: modified 5 objects (of 5), 53 properties (of 88), 0 items removed

   If the Console contains any errors, address them and click *Apply Game Table* again.
5. Optional. Save all the changes made by Game Tables via *File / Save Project*.
