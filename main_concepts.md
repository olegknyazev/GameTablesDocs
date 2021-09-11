---
title: Main Concepts
nav_order: 1
---
# Main Concepts

## Editor Mode Import

The main thing you should know about Game Tables is that it works in *editor*. It's not included in your game build and it does not load any data at runtime. Instead, it applies table data to prefabs and scriptable objects in *editor mode*. All the prefabs go into your game build with properties already updated.

Game Table is an object that resides in your project (it's a ScriptableObject from the programmer's point of view). This object contains all the settings related to a single data source which may be a single table or a group of tables in case of multi-sheet documents. You may have as many Game Table objects in your project as you need.

Import process may be triggered by a data change in case of locally stored data sources (CSV) or manually in case of online-stored data sources (Google Sheets). You may run import on any of Game Tables present in project or run it on all the Game Tables in project at once.

## Data Layout

Game Tables applies two-dimensional data to object hierarchies. To do so, it somehow maps table structure to objects. This section explain this process in details.

A table in Game Tables always have a row header, a column header and content:

|                 | Column Headers |
|:---------------:|:--------------:|
| **Row Headers** | Content        |

Content contains actual data that is applied to target objects' properties. Headers contain information that allows Game Table to figure out to which exactly property of which exactly object the data should be applied. In the simplest form column header contains a name of an object in your project and a row header contains a property name:

|          | Health | Damage |
|:---------|-------:|-------:|
| Player   | 120    | 35     |
| Enemy    | 90     | 20     |

But actually both headers may contain more information that allow you to select a property more precisely. There's four element types that a property may consist of: *Object name*, *Object path*, *Component type* and *Property name*. These elements may be split accross row and column headers which allows you to compose sophisticated table layouts like this one:

::image::

Detailed description of headers format see in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).
