---
title: Main Concepts
nav_order: 2
---
# Main Concepts

## Editor Mode Import

Game Tables works in editor mode. It is not included in your game build and does not load any data at play time. The spreadsheet data is only imported into your [Prefabs](https://docs.unity3d.com/Manual/Prefabs.html) and [ScriptableObjects](https://docs.unity3d.com/Manual/class-ScriptableObject.html) when you manually invoke commands from the Editor. Once applied, the data will go into your packaged build the same way as if it had been entered directly into your assets.

| If you're looking for a tool that updates game data in a released build, consider using [Asset Bundles](https://docs.unity3d.com/Documentation/Manual/AssetBundlesIntro.html). This way, you will not only be able to use Game Tables for updates, but also change the data that is usually not stored in spreadsheets, such as textures and sounds. |

## GameTable Object

GameTable is an object that resides in your project (it's a ScriptableObject from a programmer's point of view). This object contains all the settings related to a single data source, which can be a Google Sheets document or a CSV file in your project. You can have as many GameTable objects in your project as you need.

In the GameTable object's [Inspector]({{ site.baseurl }}{% link reference/inspector.md %}), you can find a button to import the data from this particular data source. For locally stored CSV files, there's an *Apply on Change* option that automatically re-imports data each time the source file changes. You can also re-import all the GameTables in the project at once by using the *Tools / Game Tables / Apply All Game Tables* menu.

## Sheets and Tables

The GameTable's data source, depending on its type, can contain one or more sheets. For example, a single Google Sheets document can include multiple sheets, which are displayed as tabs at the bottom of the UI.

A sheet, in turn, can contain one or more tables—continuous spans of cells that usually group together the data for a related set of objects.

![Sheets and Tables]({{ site.baseurl }}{% link sheets_and_tables.png %})

This distinction between sheets and tables gives you some flexibility in how to lay out your data. Game Tables aims to be as non-restrictive as possible, letting you organize your data in the most natural way.

| You can force Game Tables to treat the entire sheet as a single table. See the [Layout]({{ site.baseurl }}{% link reference/inspector.md %}#layout) property for details. |

## Table Structure

The table is where the actual data is stored. It's a two-dimensional grid of cells that always has the row headers, the column headers, and the content:

![Sheets and Tables]({{ site.baseurl }}{% link row_and_column_headers.png %})

Essentially, a table defines values for a *set of properties* of a *set of objects*. In the above example, *Peon*, *Grunt* and *Ogre* are objects, and *Health* and *Damage* are their properties. Similarly, you could define a table for all the hitscan weapons in your game or all the progression levels of a certain ability.

The content part contains the actual values to be applied to the target objects' properties. The column and row headers tell Game Tables where exactly these values should be applied. In a simple case, the column header can be a Prefab name and the row header can be a property name. In more sophisticated setups, both row and column headers can contain more information for more precise property selection. To learn more about headers, see [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).