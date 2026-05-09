---
parent: Reference
nav_order: 4
---
# GameTable Inspector
![Game Tables Inspector UI]({{ site.baseurl }}{% link reference/inspector.png %})

The GameTable Inspector lets you choose where the table data comes from and configure how Game Tables interprets that data when applying it to your project's assets.

## Properties

<a id="source"></a> Source Type

: Specifies where this GameTable reads its data from. Currently, local CSV files and online Google Sheets documents are supported. The properties shown directly below depend on the selected source type.

### Google Sheets Properties

These only appear if the *Source Type* is *Google Sheets*.

<a id="spreadsheet-id"></a> Spreadsheet Id

: The unique identifier of the Google Sheets document to import data from. A spreadsheet ID is a long sequence of letters and numbers and can be found in the document's URL. As a shortcut, you can paste the entire URL into this field — Game Tables will extract the ID automatically.

  To use Google Sheets documents, you must sign in to Google and grant Game Tables access to your spreadsheets. If you aren't signed in, an authorization button is shown at the bottom of the Source block. For more information, see [Authorize in Google Sheets]({{ site.baseurl }}{% link guides/authorize_in_google_sheets.md %}).

  Game Tables supports only documents in the US locale (en_US). You can change a spreadsheet's locale from the *File / Spreadsheet Settings* menu in Google Sheets.

Spreadsheet Name

: A read-only field that displays the name of the document at the specified [Spreadsheet Id](#spreadsheet-id). Use it to confirm that the ID points to the document you intended.

Sheets to Import

: A dropdown that lets you pick which sheets of the document to import. Each entry in the dropdown is checkable, so you can import any subset of the document's sheets.

  | Keep in mind that a GameTable always stores a concrete list of sheet names. The *Select All* menu item simply populates that list with all sheets currently available on the server. If sheets are later added or removed in the online document, you may need to update the list manually. |

### CSV Properties

These only appear if the *Source Type* is *CSV*.

Asset

: A reference to a .csv file in the project to import data from. The referenced asset must be a [TextAsset](https://docs.unity3d.com/Manual/class-TextAsset.html).

Apply on CSV Change

: If checked, the GameTable is automatically re-applied each time the source .csv file changes, without requiring a manual click on [Apply Game Table](#apply-game-table).

### Common Properties

<a id="orientation"></a> Orientation

: Specifies how to interpret column and row headers. In the default *Object Per Row* mode, each row corresponds to an object — its header is a Prefab name (optionally with a property prefix) — and each column corresponds to a property. The *Property Per Row* mode flips this: rows become properties and columns become objects. For more on header syntax, see [Header Format]({{ site.baseurl }}{% link reference/header_format.md %}).

<a id="layout"></a> Layout

: Specifies whether Game Tables should interpret each sheet as a single continuous table (*Single Table*) or a collection of multiple isolated tables (*Islands*). Since each table has its own row and column headers, putting multiple tables on the same sheet lets you apply properties to several different types of objects from a single sheet.

  For multi-sheet documents, this setting is applied to each sheet independently. In other words, every sheet of a document can contain several tables.

  For a group of cells to form a separate table (an *island*), it must be surrounded by a border of empty cells.

  The default mode is *Islands*.

<a id="search-path"></a> Search Path

: Specifies the root folder under which Game Tables searches for assets referenced from the table. The path is relative to the project folder and usually starts with *Assets/* (for example, *Assets/Prefabs/Buildings*).

  This folder is used both for [Prefab Names]({{ site.baseurl }}{% link reference/header_format.md %}#prefab-name) referenced in header cells and for [asset references]({{ site.baseurl }}{% link reference/data_types.md %}#asset-references) in content cells.

  If the *Is Relative* option is enabled, the path is interpreted as relative to the GameTable asset's own location. For example, if the inspected GameTable lives at `Assets/Units/AllUnits.asset`, a relative search path of *Melee* refers to the `Assets/Units/Melee` folder.

No Value Marker

: Specifies a value that, when found in a cell, marks the cell as having no value at all. A cell with no value is not the same as an empty cell. By default, an empty cell assigns an empty value to the target property — for example, a string property becomes the empty string. A cell containing the *No Value Marker*, by contrast, leaves the target property unchanged.

  This is useful when you have a group of objects that share many common properties but differ in a few. With a *No Value Marker*, you can keep all those objects in a single table:

  |          | Health | Movement Speed | Fire Range  |
  |:---------|-------:|---------------:|------------:|
  | Archer   | 120    | 35             | 14          |
  | Knight   | 90     | 20             | -           |

  In the example above, the Knight Prefab has no Fire Range property, so writing a value there would normally produce an error. The "-" in that cell is the *No Value Marker* (the default value), which tells Game Tables to skip the cell entirely.

<a id="array-update-policy"></a> Array Update Policy

: Specifies how Game Tables combines the values from the table with the existing contents of an array property. Two modes are available:

  - **Replace Whole Array** (default)
    
    The entire array is replaced with values from the table. Since the table references specific array indices, the resulting array may contain gaps where no index was referenced; those positions are filled with the default value for the property's data type (the empty string for strings, zero for numbers, and so on). For more on data types and their default values, see [Data Types]({{ site.baseurl }}{% link reference/data_types.md %}).

  - **Replace Specific Elements**
    
    Only the items at the referenced indices are replaced. Any other elements of the array remain intact.

  For more information, see [Array Update Modes]({{ site.baseurl }}{% link reference/arrays.md %}#array-update-policy).

<a id="apply-game-table"></a> Apply Game Table

: Updates the properties of all target Prefabs and ScriptableObjects with data imported from the configured source. If something goes wrong during the process, an error message is logged to the Console window and all affected objects are reverted to the state they were in before the update. A successful update can also be reverted in a single step using Unity's Undo command.

  | After an update, the affected Prefabs and ScriptableObjects are *not saved* automatically. Run *File / Save Project* to persist the changes. |
