---
parent: Reference
nav_order: 4
---
# GameTable Inspector 
![Game Tables Inspector UI]({{ site.baseurl }}{% link reference/inspector.png %})

## Properties

<a id="source"></a> Source

: Specifies the type of the table data source. Currently CSV files and Google Sheets documents are supported. The following four parameters depend on selected value.

### Google Sheets Properties

<a id="spreadsheet-id"></a> Spreadsheet Id

: A unique identifier of a Google Sheets document to import data from. Spreadsheet Id looks like a long sequence of letters and numbers. You may paste the entire URL of an Google Sheets document from the browser address bar—the interesting part will be extracted automatically.

  In order to access Google Sheets documents you need to authorize in Google and grant access for Game Tables application. In case if you have not authorized yet, a special UI will be shown below. More information about Google Sheets authrozation see in [Authorize in Google Sheets]({{ site.baseurl }}{% link guides/authorize_in_google_sheets.md %}).

Spreadsheet Name

: A read-only field that displays the name of the specified Google Sheets document. It helps you be sure that you specified the correct [Spreadsheet Id](#spreadsheet-id).

Sheets to Import

: A checklist that specifies which of the document sheets you want to import. You may use this property for multi-sheets documents to make Game Tables import only some of them.

  | Keep in mind, that a GameTable object stores a concrete list of sheets. The menu item *Select All* just updates the list to the current value got from the Google Sheets service. It does mean that if the composition of sheets is changed in the online document, existing GameTable object may require manual update. |

### CSV Properties

Asset

: A reference to a .csv file in the project to import data from. The referenced asset should be [TextAsset](https://docs.unity3d.com/Manual/class-TextAsset.html).

Apply on CSV Change

: If checked, the GameTable will be re-applied each time the source .csv file is changed.

### Common Properties

<a id="orientation"></a> Orientation

: Specifies how to interpret column and row headers. The default mode is *Object Per Row* in which case row headers are considered Prefab names (with optional property prefixes) and column headers are considered as property names. The *Property Per Row* mode "flips" the table. More on row and columns headers see in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).

<a id="layout"></a> Layout

: Specifies whether Game Tables should interpret the whole sheet as a single table or a collection of multiple isolated tables. Each table has separate row and column headers. By using *Islands* mode you can define properties for objects of different types in a single sheet. The *Single Table* mode supposes that the whole sheet has a single heading row and a single heading column.

  For multisheet documents (e.g. Google Sheets documents) this property is applied to each sheet. That is, you may have several sheets in a document and each of these sheets may contain several tables.

  To make part of a sheet an island, separate it from the surroundings by a border of empty cells.

  The default value is *Islands*.

<a id="search-path"></a> Search Path

: Specifies the root folder for searching assets that are referenced from the table. The path is relative to the project root folder and usually starts with *Assets/* (e.g. *Assets/Prefabs/Buildings*).

  This folder is used for assets specified in either header or content rows. More on referencing assets from another assets see in [Asset References]({{ site.baseurl }}{% link reference/data_types.md %}#asset-references).

No Value Marker

: Specifies a value that may be used in the table to mark cells that do not have a value. Not having a value is not the same as empty cell. By default, if a cell is empty, then an empty value will be assigned to the property. But if cell contain "no value" marker value, property will not be changed at all.

  This may be useful when you have a group of objects having many common properties but a few different properties. By using *No Value Marker* you may put all these objects into a single table:

  |          | Health | Movement Speed | Fire Range  |
  |:---------|-------:|---------------:|------------:|
  | Archer   | 120    | 35             | 14          |
  | Knight   | 90     | 20             | -           |

  In the above example Knight Prefab does not have Fire Range property so it's an error to specify Fire Range for Knight. But if you put a special *No Value Marker* value into the Fire Range cell, Game Tables will ignore it.

Array Update Policy

: Specifies how Game Tables should treat array updates. There are two modes available:

  - **Replace Whole Array** (default)
    
    In this mode, if an array property is referenced from a table, it's replaced entirely. Because you always refer a specific array element from a table, it's possible to have holes in the array after an update. These holes are assigned to the default value for a specific data type (empty string for strings, zero for numbers etc.). For more on data types and their default values see [Data Types]({{ site.baseurl }}{% link reference/data_types.md %}).

  - **Replace Specific Elements**
    
    In this mode, if an array property is referenced from a table, only items at the referenced indices are replaced.

  More information on this property see in [Array Update Modes]({{ site.baseurl }}{% link reference/headers_format/arrays.md %}).

<a id="apply-game-table"></a> Apply Game Table

: Updates properties of all the target Prefabs and ScriptableObject by data imported from the specified table source. If something goes wrong during the applying, an error message is shown in the Console window and all the affected objects are reverted to the state they had before the update. A successful application may be reverted in a single step by Unity's Undo menu.

  After an update all the affected Prefabs are *not saved* automatically. You need to run *File / Save Project* to persist the changes.
