---
parent: Guides
nav_order: 2
---
# Import From Google Sheets
To set up importing from Google Sheets, perform the following actions:
1. Create a GameTable object (right click on Project window, *Create / Game Tables / Game Table*).
2. Set up the GameTable object properties:
    1. Choose *Google Sheets* in the [Source]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdown.
    2. Copy URL of a Google Sheets document into the [Spreadsheet Id]({{ site.baseurl }}{% link reference/inspector.md %}#spreadsheet-id) field. You can also paste just the id part here.
    3. If the specified document has a locale that's differ from United States (en_US) you have to change it in the *File / Spreadsheet Settings* menu.
    4. If you're connecting Game Tables to Google Sheets for the first time, you will be prompted to authorize in Google and grant Game Tables application read access to your Google Documents. See [Authorize In Google Sheets]({{ site.baseurl }}{% link guides/authorize_in_google_sheets.md %}) for details.
    5. Enter into the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) text box a path to the folder containing Prefabs the spreadsheet refers on. The path is specified relative the project root, for example *Assets/Prefabs/Units*.
    6. Optional. Specify additional settings that alter the way the table data should be interpreted. For example, you may choose whether to use object-per-row or property-per-row layout. For more see [GameTable Inspector]({{ site.baseurl }}{% link reference/inspector.md %}).
3. Click [Apply Game Table]({{ site.baseurl }}{% link reference/inspector.md %}#apply-game-table). 
4. Check the Console window. If everything gone well, it should contain a message like the following:
   > Game Tables: modified 5 objects (of 5), 53 properties (of 88), 0 items removed

   If the Console contains any errors, fix their causes and then click Apply Game Table again.
5. Optional. Save all the changes made by Game Tables by clicking *File / Save Project* menu.