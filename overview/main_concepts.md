---
parent: Overview
title: Main Concepts
nav_order: 1
---
# Main Concepts
The main thing you should know about Game Tables is that it works in *editor*. It's not included in your game build and it does not load any data at runtime. Instead, it applies table data to prefabs and scriptble objects in *editor mode*. All the prefabs go into your game build with properties already updated.

Game Table is an object that resides in your project (it's a ScriptableObject from the programmer's point of view). This object contains all the settings related to a single data source which may be a single table or a group of tables in case of multi-sheet documents. You may have as many Game Table objects in your project as you need.

Import process may be triggered by a data change in case of locally stored data sources (CSV) or manually in case of online-stored data sources (Google Sheets). You may run import on any of Game Tables present in project or run it on all the Game Tables in project at once.