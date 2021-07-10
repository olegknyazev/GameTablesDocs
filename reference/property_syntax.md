---
parent: Reference
title: Property Syntax
nav_order: 1
---
# Property Syntax
When importing data from a table, Game Tables needs to know how to map a property specified a table to a prefab. Prefab is a complex thing: it’s a hierarchy of objects each of which may have components, each of which may have properties. Properties may be nested into each other. 

When searching for a matching property, Game Tables tried to do most intuitive thing: find any property that matches specified name, if there is exactly one of those, everything is good: apply it. But if there’s more than one property matches, you have to specify more explicitly to which part of prefab it should be applied. To do so Game Tables supports rich syntax for properties. Of course, you can use it even when there’s no ambiguity, if you want to be explicit.

!! format description