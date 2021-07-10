---
parent: Guides
nav_order: 1
---
# Import from Google Sheets
To set up importing from Google Sheets, perform the following actions:
1. Create a Game Table object.
2. Set up the Game Table object properties:
    1. Choose Google Sheet as Source.
    2. Copy link to your Google Sheet table into Spreadsheet Id field. Spreadsheet Id will be extracted automatically.
    3. Specify where to search for prefabs whose properties should be updated by the data from a Google Sheet.
    4. Optional. Specify additional settings that alter the way table data is interpreted. For example, you may choose which sheets should be user and whether to use object-per-row or property-per-row layout. For more see !!!
3. Run update. If something goes wrong, check out Console window. If any error occurred, any data leaved untouched. Change is recorded to undo history - you may rollback it back and reapply if you want.
4. Whenever you updated the Google Sheet and want these changes to be applied to Unity project, run update again. You also may use menu Tools / Game Tables / !!! to update all Game Tables at once. Game Tables doesn’t apply Google Sheets changes automatically, see the section !!! for details.