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

Notice the **/** separator between *Prefab Name* and the following header components. It's required if a row header contains any components besides *Prefab Name*. Otherwise it would be impossible to distinguish the extra components from *Prefab Name* due to whitespace-insensitivity of Game Tables.

More details on specific header components see in [Header Components](#header-components).

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

## Header Components

There are four types of components that may be used in row and column headers: *Prefab Name*, *Game Object Name*, *Component Type* and *Property Path*.

An important thing is that these components *always* go in order, i.e. you cannot specify *Component Type* after *Property Path*. This rule is applyable even when these components split between row and column headers. In this case the row header is considered as a prefix for the column header.

The only required components that any cell should contain are *Prefab Name* and *Property Path*.

It does not matter for Game Tables how exactly you split the required components by row and column headers. So, the following compositions actually refer the same property:

| Player / Gun \<Clip\> Bursts[0] | Pellet Count |

| Player / Gun \<Clip\> | Bursts[0].Pellet Count |

| Player | Gun \<Clip\> Bursts[0].Pellet Count |

### Prefab Name

Object name locates Prefab or Scriptable Object inside the project. It's a simple name that Game Tables looking for in the Search Path specified in a Game Table object. It should not contain file extension or any hierarchical components.

### Game Object Name

Subobject path locates a Game Object inside a prefab. It's only appliable to prefabs, when applying a property to a Scriptable Object, it's a mistake to include subobject path.

Subobject path is a hierarchical name

**TODO is partial matching supported here?**

### Component Type

Component type restricts a property to specific component of a Game Object.

### Property Name

## Case- and Whitespace Sensitivity

All the path components are both case- and whitespace insensitive. When looking for an object or its property, Game Tables converts both actual property name and the name, specified in a table, to lower registry and removes all the whitespace. After this comparison happen. So, all the following property paths actually refer to the same property:
- `Cluster Mine / <Spreading Spawner> Targets[0].Offset.X`
- `ClusterMine/<SpreadingSpawner>Targets[0].Offset.X`
- `clustermine/<spreadingspawner>targets[0].offset.x`

## Partial Matching

When matching a property path against an actual objects and properties ...
