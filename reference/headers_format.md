---
parent: Reference
title: Headers Format
nav_order: 1
---
# Headers Format

When Game Tables sees a value in a table cell, it should determine to which property of which object it should be applied. To do so, it checks the content of the row and column headers corresponding to this cell. The headers may contain one or more *path components*.

## Path components

There are four types of path compnents: *Object name*, *Subobject path*, *Component type* and *Property name*. These components may be split between row and column headers in various proportion:

::image::

All the components should go in order but only the *Object name* and *Property name* are required. So the following are examples of valid headers:

::image::

It does not matter for Game Tables how exactly you split the required components by row and column headers. So, the following compositions actually refer the same property:

::image::

**TODO explain what Game Tables does for duplicates**

### Object Name

Object name locates Prefab or Scriptable Object inside the project. It's a simple name that Game Tables looking for in Search Path specified in Game Table object. It should not contain file extension or any hierarchical components.

### Subobject Path

Subobject path locates a Game Object inside a prefab. It's only appliable to prefab object, when applying property to a Scriptable Object, it's a mistake to include subobject path.

Subobject path contains of Game Object names that forms ...

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
