---
title: About
nav_order: 0
---
# About
**Game Tables** is a Unity plugin for importing spreadsheet data into your [Prefabs](https://docs.unity3d.com/Manual/Prefabs.html) and [ScriptableObjects](https://docs.unity3d.com/Manual/class-ScriptableObject.html). It works with online Google Sheets documents and locally stored CSV files.

### How It Works
You create a GameTable asset, point it at a spreadsheet, and import the values into the referenced Prefabs and ScriptableObjects. The imported data is applied to your assets at edit time, so the game build doesn't contain any Game Tables code.

### Key Features
- imports from Google Sheets without setting up any developer accounts or API keys
- doesn't require writing any code
- supports common property types such as numbers, strings and vectors as well as your custom `[Serializable]` structs and classes
- handles arrays and nested structures

If you're here for the first time, check out these pages:
- [Getting Started]({{ site.baseurl }}{% link getting_started.md %})—explains the package structure and the included example
- [Main Concepts]({{ site.baseurl }}{% link main_concepts.md %})—covers the key concepts behind Game Tables
- [Guides]({{ site.baseurl }}{% link guides/index.md %})—step-by-step walkthroughs for typical tasks