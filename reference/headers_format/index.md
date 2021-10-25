---
parent: Reference
nav_order: 1
has_children: true
--- 
# Headers Format

When Game Tables sees a value in a table cell, it should determine to which property of which object it should be applied. To do so, it checks the content of the row and column headers corresponding to this cell.

As a general rule, you may think that a row header locates an object and a column header locates a property inside the object.


| You may flip the table by setting *Orientation* property of a *Game Table* to *Object Per Column*. The documentation always refers to row and column headers supposing than *Orientation* is set to its default value — *Object Per Row*.|

## Row Headers

The full syntax of a row header is following:
> **Prefab Name** [ / [*Game Object Name*] [<*Component Type*>] [*Property Prefix*]]

*Square brackets denote optional clauses.*

A row header should conform the following rules:
* Must contain a *Prefab Name*
* May contain a *Game Object Name* if the column header does not contain it
* May contain a *Component Type* if the column header does not contain it nor *Game Object Name*
* May contain a prefix for *Property Path* if the column header does not contain *Game Object Name* or *Component Type*

Examples:
* Player
* Big Soldier / Gun
* Yellow Car / Front Left Wheel \<Rigid Body\>
* Plasma Gun / \<Shooter\> Patterns[0].Offset

Notice the **/** separator between *Prefab Name* and the following header elements. It's required if a row header contains any elements besides *Prefab Name*. Otherwise it would be impossible to distinguish the extra elements from *Prefab Name* due to [whitespace-insensitivity]({{ site.baseurl }}{% link reference/headers_format/matching_rules.md %}#case--and-whitespace-sensitivity) of Game Tables.

More details on specific header elements see in [Header Elements]({{ site.baseurl }}{% link reference/headers_format/header_elements.md %}).

## Column Headers

The full syntax of a column header is following:
> [*Game Object Name*] [<*Component Type*>] **Property Path**

*Square brackets denote optional clauses.*

A column header should conform the following rules:
* Must contain a *Property Path* or its suffix
* May contain *Game Object Name* if the row header does not contain it nor *Component Type*
* May contain *Component Type* if the row header does not contain it

Examples:
* Health
* \<Clip\> Ammo
* Spawn Point 1 / \<Spawner\> Offset.X
