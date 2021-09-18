---
parent: Guides
nav_order: 1
---
# Import From Google Sheets
To set up importing from Google Sheets, perform the following actions:
1. Create a Game Table object.
2. Set up the Game Table object properties:
    1. Choose *Google Sheets* in the [Source]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdown.
    2. Copy URL (link) of your Google Sheet table into the [Spreadsheet Id]({{ site.baseurl }}{% link reference/inspector.md %}#spreadsheet-id) field. The actual id will be extracted automatically. You also can paste just the id part here, if you like.
    3. If you're connecting Game Tables to Google Sheets for the first time, you will be asked to authorize in Google and grant Game Tables application read access for your Google Documents. For more details about this process see [Google Sheets Authorization]({{ site.baseurl }}{% link reference/google_sheets_authorization.md %}).
    4. Fill the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) text box with a path to the folder containing Prefabs you want to modify or refer from the spreadsheet. The path is specified relative the project root, for example *Assets/Prefabs/Units*.
    5. Optional. Specify additional settings that alter the way the table data is interpreted. For example, you may choose to import only from specified sheets (for multisheet document) and whether to use object-per-row or property-per-row layout. For more see [Inspector]({{ site.baseurl }}{% link reference/inspector.md %}).
3. Click [Update Targets]({{ site.baseurl }}{% link reference/inspector.md %}#update-targets). Successful attempt is recorded to the undo history - you may rollback it back and reapply if you want. Unsuccessful attempt leaves all the assets as they were before the update. In this case Console window will contain a detailed description of occured problems. Be aware that modified assets are **not** saved automatically. To do so run *File / Save Project* menu.
4. Whenever you updated the spreadsheet and want these changes to be applied to your project, run Update Targets again. You also may use menu *Tools / Game Tables / Update All Tables* to update all the Game Tables in the project at once. Game Tables doesn’t apply Google Sheets changes automatically.