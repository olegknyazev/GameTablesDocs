---
title: Main Concepts
nav_order: 2
---
# Main Concepts

## Editor Mode Import

Game Tables works in editor mode. It's not included in your game build and it does not load any data at play time. Instead, it applies spreadsheet data to [Prefabs](https://docs.unity3d.com/Manual/Prefabs.html) and [ScriptableObjects](https://docs.unity3d.com/Manual/class-ScriptableObject.html) while you're working in Editor. All the assets go into your game build with properties already updated from spreadsheet.

| If you're looking for a tool that updates game data in a released build, consider using [Asset Bundles](https://docs.unity3d.com/Documentation/Manual/AssetBundlesIntro.html). |

## GameTable Object

GameTable is an object that resides in your project (it's a [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html) from the programmer's point of view). This object contains all the settings related to a single data source which may be a single table or a group of tables in case of multi-sheet documents. You may have as many GameTable objects in the project as you need.

You may run import from GameTable object's [Inspector]({{ site.baseurl }}{% link reference/inspector.md %}). For locally stored data source (CSV) it's also possible to enable auto-import which automatically re-imports data each time the source file changes. You also may re-import all the GameTables in the project at once by using the *Tools / Game Tables / Apply All Game Tables* menu.

## Sheet

A sheet is a two-dimensional data container that consists of cells. For CSV files, single CSV file is a single sheet. For Google Sheets documents, single document may consist of several sheets.

A sheet may contain one or more tables. For example, you may have a sheet that defines data for different types of objects which may be convenient if these objects share some common calculations or intermediate data. Each table in a sheet should be separated from any other by at least one empty cell at each side.

![Sheets and Tables]({{ site.baseurl }}{% link sheets_and_tables.png %})

| Multi-table functionallity may be disabled, see the [Layout]({{ site.baseurl }}{% link reference/inspector.md %}#layout) GameTable property for details. |

## Table

A table is a continuous grid of cells that usually contains data for a related set of objects. For example, you may have a table for all the hitscan weapons in your game or all the progression levels of a skill. Essentially, a table allows you to define a *set of properties* for a *set of objects* (that's what two-dimensionality means).

A table always have the row headers, the column headers and the content:

|                  | Column Header 1 | Column Header 2 | ... |
|:----------------:|:---------------:|:---------------:|:---:|
| **Row Header 1** | Content         | Content         | ... |
| **Row Header 2** | Content         | Content         | ... |
| **...**          | ...             | ...             | ... |

Content contains actual data that is applied to the target objects' properties. Column and row headers contain information that allows Game Tables to figure out to which exactly property of which exactly object the data should be applied. In the simplest case the column header is a name of Prefab in your project and the row header is a property name:

|          | Health | Damage |
|:---------|-------:|-------:|
| Player   | 120    | 35     |
| Enemy    | 90     | 20     |

:: TODO add inspect image here? ::

But actually both row and column headers may contain more information that allow you to select a property more precisely. The detailed description of headers format see in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).
