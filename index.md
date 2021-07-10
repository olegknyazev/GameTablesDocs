---
nav_order: 0
---
# Overview
Game Tables is a Unity plugin that imports prefab properties from table sources: online Google Sheets pages or locally stored CSV files.

*Why would you need it?*

Unity has a very powerful serialisation mechanism that allows you put your data right into prefabs and get this data loaded at run-time automatically. If you have a Game Object in a scene, when the game starts, according .NET objects will be created and all their properties will be magically set to the values specified in Inspector. It’s huge time saver and it’s great from the programmer’s point of view. But for some data the table format works just better. For example, consider situation where you have several upgrades that a player may purchase in a game. And you want to balance them. It may be too cumbersome to do this by setting properties in Inspector. Professional game designers often use table tools for these tasks: Excel, Google Sheets. By using this tool you may easily enter some formulas and get the values for all the upgrade levels at once. Or you may enter another formula and infer how much time it would take to kill an enemy at every upgrade level.

So, Game Tables builds a bridge between programming and game design worlds by importing data from a table and automatically applying it to prefabs in your project. Currently, it works with Google Sheets and CSV data sources.