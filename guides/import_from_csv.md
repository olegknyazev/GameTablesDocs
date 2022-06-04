---
parent: Guides
nav_order: 1
---
# Import from CSV
To set up importing from a CSV file, perform the following actions:
1. Create a GameTable object (right click on Project window then *Create / Game Tables / Game Table*).
2. Set up the GameTable object properties:
    1. Choose *CSV* in the [Source]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdown.
    2. Specify a CSV file [Text Asset](https://docs.unity3d.com/Manual/class-TextAsset.html) from which the data should be imported.
    3. Fill the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) text box with a path to the folder containing Prefabs the CSV file refers on. The path is specified relative the project root, for example *Assets/Prefabs/Units*.
    4. Optional. Specify additional settings that alter the way the table data should be interpreted. For example, you may choose whether to use object-per-row or property-per-row layout. For more see [GameTable Inspector]({{ site.baseurl }}{% link reference/inspector.md %}).
3. Click [Apply Game Table]({{ site.baseurl }}{% link reference/inspector.md %}#apply-game-table). 
4. Check the Console window. If everything gone well, it should contain a message like the following:
   > Game Tables: modified 5 objects (of 5), 53 properties (of 88), 0 items removed

   If the Console contains any errors, fix their causes and then click Apply Game Table again.
5. Optional. Save all the changes made by Game Tables by clicking *File / Save Project* menu.