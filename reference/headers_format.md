---
parent: Reference
title: Headers Format
nav_order: 1
---
# Headers Format

When Game Tables sees a value in a table cell, it should determine to which property of which object it should be applied. To do so, it checks the content of the row and column headers corresponding to this cell.

As a general rule, you may think that a row header locates an object and a column header locates a property inside this object.

> You may flip the table by setting *Orientation* property of a *Game Table* to *Object per Column*. The documentation always refers to row and column headers supposing than *Orientation* is set to its default value — *Object per Row*.

## Row Headers

The full syntax of a row header is following:
> **Prefab Name** [ / [*Game Object Name*] [<*Component Type*>] [*Property Prefix*]]

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

Notice the **/** separator between *Prefab Name* and the following header elements. It's required if a row header contains any elements besides *Prefab Name*. Otherwise it would be impossible to distinguish the extra elements from *Prefab Name* due to whitespace-insensitivity of Game Tables.

More details on specific header elements see in [Header Elements](#header-elements).

## Column Headers

The full syntax of a column header is following:
> [*Game Object Name*] [<*Component Type*>] **Property Path**

A column header should conform the following rules:
* Must contain a *Property Path* or its suffix
* May contain *Game Object Name* if the row header does not contain it nor *Component Type*
* May contain *Component Type* if the row header does not contain it

Examples:
* Health
* \<Clip\> Ammo
* Spawn Point 1 / \<Spawner\> Offset.X

## Header Elements

There are four types of elements that may be used in row and column headers: *Prefab Name*, *Game Object Name*, *Component Type* and *Property Path*.

An important thing is that these elements *always* go in order, i.e. you cannot specify *Component Type* after *Property Path*. This rule is applyable even when these elements split between row and column headers. In this case the row header is considered as a prefix for the column header.

The only required elements that any cell should contain are *Prefab Name* and *Property Path*.

It does not matter for Game Tables how exactly you split the required elements by row and column headers. So, the following compositions actually refer the same property:

| Player / Gun \<Clip\> Bursts[0] | Pellet Count |

| Player / Gun \<Clip\> | Bursts[0].Pellet Count |

| Player | Gun \<Clip\> Bursts[0].Pellet Count |

The following subsections describes header element types in details.

### Prefab Name

*Prefab Name* locates a prefab or a scriptable object inside the project. Game Tables searches for this name recursively starting from the directory specified in the *Search Path* property of a *Game Table* object.

A *Prefab Name* should be a simple name, it cannot contain any hierarchy.

A *Prefab Name* must be specified in a row header.

Examples:
* Burst Rifle
* Level 1 AI Settings

### Game Object Name

*Game Object Name* path locates a Game Object inside a prefab. Game Tables searches for this name recursively starting from the prefab's root game object.

*Game Object Name* is only appliable to prefabs, it should not be used in cells that target scriptable objects.

*Game Object Name* should be a simple name, it cannot contain any hierarchy.

*Game Object Name* is optional, you may omit it from both row and column headers.

Example:
* Spawn Point 1
* Muzzle

**TODO is partial matching supported here?**

### Component Type

*Component Type* locates a component inside a game object. Because game object may contain several components, a simple property name may be ambiguous. So, *Component Type* allows you to specify to which exactly component the property should be applied.

*Component Type* is only appliable to prefabs, it should not be used in cells that target scriptable objects.

When *Game Object Name* is not specified, Game Tables searches for the required component and property combination in all the game objects inside a prefab.

*Component Type* is optional, you may omit it from both row and column header.

To distinguish *Component Type* from other elements it's enclosed in angle brackets. Example:
* \<Rigid Body\>
* \<Enemy Brain\>

### Property Path

*Property Path* locates a specific property inside a component or scriptable object. *Property Path* may be hierarchical and contain array indexers and [wildcard indexers](#wildcard-indexers).

A *Property Path* may be combined from row and column headers. In this case content of a column header is added to the end of the row header:

| Row Header | Column Header | Result
|-|-|-
| Position      | X             | Position.X
| Patterns[0]   | Spread.Power  | Patterns[0].Spread.Power

*You may notice that in some cases the **.** separator was added to the result to disnguish path elements.*

A *Property Path* or its suffix must be specified in a column header.

Examples:
* Position.X
* Waves[0].Enemies to Spawn
* Spawn Points[*].Position

## Case- and Whitespace Sensitivity

All the path elements are both case- and whitespace insensitive. When looking for an object or its property, Game Tables converts both actual property name and the name, specified in a table, to lower registry and removes all the whitespace. After this comparison happen. So, all the following property paths actually refer to the same property:
- `Cluster Mine / <Spreading Spawner> Targets[0].Offset.X`
- `ClusterMine/<SpreadingSpawner>Targets[0].Offset.X`
- `clustermine/<spreadingspawner>targets[0].offset.x`

## Partial Matching

When matching a property path against an actual objects and properties ...

## Wildcard Indexers