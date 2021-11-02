---
grand_parent: Reference
parent: Headers Format
nav_order: 1
---
# Header Elements

There are four types of elements that may be used in row and column headers: *Prefab Name*, *Game Object Name*, *Component Type* and *Property Path*.

An important thing is that these elements *always* go in the specified order, i.e. you cannot put *Component Type* after *Property Path*. This rule is applicable even when these elements are split between row and column headers. In this case the row header is considered a prefix for the column header.

The only required elements that any cell should contain are *Prefab Name* and *Property Path*.

It does not matter for Game Tables how exactly you split the required elements between row and column headers. So, the following compositions actually refer the same property:

| Player / Gun \<Clip\> Bursts[0] | Pellet Count |

| Player / Gun \<Clip\> | Bursts[0].Pellet Count |

| Player | Gun \<Clip\> Bursts[0].Pellet Count |

The following subsections describe header element types in details.

## Prefab Name

*Prefab Name* locates a [Prefab](https://docs.unity3d.com/Manual/Prefabs.html) or a [ScriptableObject](https://docs.unity3d.com/Manual/class-ScriptableObject.html) inside the project. Game Tables searches for this name recursively starting from the directory specified in the *Search Path* property of a GameTable object.

Prefab Name should be a *simple* name, it cannot contain any hierarchy.

Prefab Name must be specified in a *row header*.

Examples:
* Burst Rifle
* Level 1 AI Settings

## Game Object Name

*Game Object Name* path locates a Game Object inside a Prefab. Game Tables searches for this name recursively starting from the Prefab's root game object.

Game Object Name is only appliable to *Prefabs*, it should not be used in cells that target ScriptableObjects.

Game Object Name should be a *simple name*, it cannot contain any hierarchy.

Game Object Name is *optional*, you may omit it from both row and column headers.

Example:
* Spawn Point 1
* Muzzle

**TODO is partial matching supported here?**

## Component Type

*Component Type* locates a component inside a game object. Because game object may contain several components, a simple property name may be ambiguous. So, *Component Type* allows you to specify the exact component type the property should be applied to. When *Game Object Name* is not specified, Game Tables searches for the required component and property combination in all the game objects inside a Prefab.

Component Type is only appliable to *Prefabs*, it should not be used in cells that target ScriptableObjects.

Component Type is *optional*, you may omit it from both row and column header.

To distinguish *Component Type* from other elements it's enclosed in angle brackets. Example:
* \<Rigid Body\>
* \<Enemy Brain\>

## Property Path

*Property Path* locates a specific property inside a component or ScriptableObject. *Property Path* may be hierarchical and contain array indexers and [wildcard indexers](#wildcard-indexers).

Property Path may be combined from row and column headers. In this case content of a column header is added to the end of the row header:

| Row Header | Column Header | Result
|-|-|-
| Position      | X             | Position.X
| Patterns[0]   | Spread.Power  | Patterns[0].Spread.Power

*You may notice that in some cases the **.** separator was added to the result to distinguish path elements.*

Property Path or its suffix must be specified in a *column header*.

Examples:
* Position.X
* Waves[0].Enemies to Spawn
* Spawn Points[*].Position
