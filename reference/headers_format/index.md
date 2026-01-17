---
parent: Reference
nav_order: 1
has_children: true
--- 
# Headers Format

When Game Tables processes a value in a table cell, it needs to determine to which property of which object the value should be applied. To do so, it checks the content of the row and column headers corresponding to the cell.

As a general rule, you may think that a row header locates the object, and a column header locates the property inside the object.

| You can flip the table by setting GameTable's [Orientation]({{ site.baseurl }}{% link reference/inspector.md %}#orientation) to *Object Per Column*. For simplicity, this documentation assumes that the default value of *Object Per Row* is used. If you use a different setting, just read "row headers" as "column headers" and vice versa. |

## Row Headers

The full syntax of a row header is the following:
> **Prefab Name** / *Game Object Name* / <*Component Type*> *Property Prefix*

The only required component of a row header is *Prefab Name*. The rest can be omitted.

Examples:
* Player
* Big Soldier / Gun
* Yellow Car / Front Left Wheel / \<Rigid Body\>
* Plasma Gun / \<Shooter\> Patterns[0].Offset

Notice the use of separators in the examples above. They must be used after *Prefab Name* and *Game Object Name* when specifying subsequent components.

## Column Headers

The full syntax of a column header is the following:
> *Game Object Name* / <*Component Type*> **Property Path**

The only required component of a column header is *Property Path*. The rest can be omitted.

Examples:
* Health
* \<Clip\> Ammo
* Spawn Point 1 / \<Spawner\> Offset.X

## Combining Row and Column Headers

To locate the property in the project, Game Tables combines the row and column headers of each cell:

![Sheets and Tables]({{ site.baseurl }}{% link reference/full_property_example.png %})

The combined header of the encircled cell is:

> Boss / Rocket Launcher / \<Health\> Armor Class

This combined header will be used to locate the object's property in the project. Game Tables gives you some flexibility in how the necessary information is split between row and column headers. For example, the below combinations of different row and column headers all point to the same object property:

| Row Header                        | Column Header                         |
|----------------------------------:|:--------------------------------------|
| Player / Gun / \<Clip\> Bursts[0] | Pellet Count                          |
| Player / Gun / \<Clip\>           | Bursts[0].Pellet Count                |
| Player                            | Gun / \<Clip\> Bursts[0].Pellet Count |

The combined header must adhere to the following rules:
* The same component can only be present in either row or column header, but not both of them. For example, if the row header contains a *Component Type*, the column header cannot also contain it. The exception to this is *Property Path*. If this component is present in the row header, it is treated as a prefix for the column's one.
* The column header (suffix) must be at least as specific as the row header (prefix). For example, if the row header contains a *Component Type*, the column header cannot contain *Game Object Name* as it is less specific than *Component Type*.

Essentially, header components can only appear in the following order in the combined header:
1. *Prefab Name*
2. *Game Object Name*
3. *Component Type*
4. *Property Path*
