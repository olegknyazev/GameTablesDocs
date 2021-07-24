---
title: Main Concepts
nav_order: 1
---
# Main Concepts

## Editor Mode Import

The main thing you should know about Game Tables is that it works in *editor*. It's not included in your game build and it does not load any data at runtime. Instead, it applies table data to prefabs and scriptble objects in *editor mode*. All the prefabs go into your game build with properties already updated.

Game Table is an object that resides in your project (it's a ScriptableObject from the programmer's point of view). This object contains all the settings related to a single data source which may be a single table or a group of tables in case of multi-sheet documents. You may have as many Game Table objects in your project as you need.

Import process may be triggered by a data change in case of locally stored data sources (CSV) or manually in case of online-stored data sources (Google Sheets). You may run import on any of Game Tables present in project or run it on all the Game Tables in project at once.

## Data Layout

Game Tables applies two-dimensional data to object hierarchies. To do so, it somehow maps table structure to objects. This section explain this process in details.

A table in Game Tables always have a row header, a column header and content:

::image::

Content contains actual data that is applied to target objects' properties. Headers contain information that allows Game Table to figure out to which exactly property of which exactly object the data should be applied. In the simplest form column header contains names of object in your project and row header contains names of properties of these object:

::image::

But actually Game Tables data mapping is a bit more powerful and lets you to express layouts like this one:

::image::

## Property Path -- ?

One of the key concepts of Game Tables is a *property path*. Each cell in the content part of a table is associated with a property path. The propery path is combined from row and column headers corresponding to the cell:

::image::

The property path may contain the following elements:
1. *Object name* which locates a prefab or scriptable object in a project: `Enemy`, `Sword of Truth`
2. *Object path* which specifies a game object inside a prefab: `/ Wheel Front Left / Tire`, `/ Weapon`
3. *Component type* which lets to restrict the component a property should be applied to: `<Movement>`, `<PhysicsBody>`
4. *Property name* which determines exact property inside a object: `Velocity`, `Rotation.Y`, `Targets[0].Position.X`

In its general form property has the following syntax:
```
Name/ [SubObject/]* [<Component>] Property[.SubProperty]*
```

For more details on property syntax see [Property Path Syntax]({{ site.baseurl }}{% link reference/property_path_syntax.md %}).

As was stated before, the property path is combined from row (*prefix*) and column (*suffix*) headers. Game Tables leaves you some freedom in deciding which parts of a property path go to prefix and which to suffix, but some restrictions are applied:
- Prefix of a property may contain *object name*, *object path* and *component type* (elements 1-3)
- Suffix of a property may contain *object path*, *component type* and *property name* (elements 2-4)
- Prefix and suffix cannot overlap (elements 1-2 plus 3-4 is ok while 1-3 plus 3-4 is not). For example, if prefix contains a *component type*, then suffix cannot contain neither *object path* nor *component type*
