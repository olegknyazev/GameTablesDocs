---
parent: Reference
title: Property Path Syntax
nav_order: 1
---
# Property Path Syntax
The general property path syntax is following:
```
Name/ [SubObject/]* [<Component>] Property[.SubProperty]*
```

Property path is combined from *prefix* and *suffix*. By default, the prefix is taken from a row header cell and the suffix is taken from a column header cell, but it may be changed by Table Layout property of a Game Table object.

The slash that divides *Name* from other parts of a property path is not necessary when a split between suffix and prefix is go right after name.

**TODO not necessary or forbided?**

Examples:
- `Player / Gun <Clip> Ammo`
- `Capture The Flag / Captures To Win`
- `Cluster Mine / <Spreading Spawner> Targets[0].Offset.X`

## Case- and Whitespace Sensitivity

All elements of a property path are both case- and whitespace insensitive. When comparing properties, Game Tables converts both actual object and property name and the name, specified in a table, to lower registry and removes all the whitespace. After this comparison happen. So, all the following property paths actually refer to the same property:
- `Cluster Mine / <Spreading Spawner> Targets[0].Offset.X`
- `ClusterMine/<SpreadingSpawner>Targets[0].Offset.X`
- `clustermine/<spreadingspawner>targets[0].offset.x`

## Partial Matching

When matching a property path against an actual objects and properties ...

## Subobject Path

Subobject path locates a Game Object inside a prefab. It's only appliable to prefab object, when applying property to a Scriptable Object, it's a mistake to include subobject path.

Subobject path contains of Game Object names that forms ...

**TODO is partial matching supported here?**

## Component Type

Component type restricts a property to specific component of a Game Object.

## Property Name
