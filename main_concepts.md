---
title: Main Concepts
nav_order: 2
---
# Main Concepts

## Editor Mode Import

The main thing you should know about Game Tables is that it *works in editor*. It's not included in your game build and it does not load any data at runtime. Instead, it applies table data to [Prefabs](https://docs.unity3d.com/Manual/Prefabs.html) and [ScriptableObjects](https://docs.unity3d.com/Manual/class-ScriptableObject.html) in *editor mode*. All the Prefabs go into your game build with properties already updated.

## GameTable Object

GameTable is an object that resides in your project (it's a [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html) from the programmer's point of view). This object contains all the settings related to a single data source which may be a single table or a group of tables in case of multi-sheet documents. You may have as many GameTable objects in the project as you need.

You may run import from the GameTable object [Inspector]({{ site.baseurl }}{% link reference/inspector.md %}). For locally stored data source (CSV) it's also possible to enable auto-import feature which automatically re-imports the data when the source table changes. You also may re-import all the GameTables in the project at once by using the *Tools / Game Tables / Apply All Game Tables* menu.

## Data Layout

Game Tables applies two-dimensional data to object hierarchies. To do so, it somehow maps table structure to objects.

A table in Game Tables always have a row header, a column header and content:

|                  | Column Header 1 | Column Header 2 | ... |
|:----------------:|:---------------:|:---------------:|:---:|
| **Row Header 1** | Content         | Content         | ... |
| **Row Header 2** | Content         | Content         | ... |
| **...**          | ...             | ...             | ... |

Content contains actual data that is applied to target objects' properties. Headers contain information that allows Game Tables to figure out to which exactly property of which exactly object the data should be applied. In the simplest form a column header contains a name of a Prefab in your project and a row header contains a property name:

|          | Health | Damage |
|:---------|-------:|-------:|
| Player   | 120    | 35     |
| Enemy    | 90     | 20     |

But actually both headers may contain more information that allow you to select a property more precisely. There's four element types that a property may consist of: *Object name*, *Object path*, *Component type* and *Property name*. These elements may be split accross row and column headers which allows you to compose sophisticated table layouts like this one:

::image::

Detailed description of headers format see in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).
