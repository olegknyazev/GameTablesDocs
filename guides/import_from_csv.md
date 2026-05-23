---
parent: Guides
nav_order: 1
---
# Import from CSV
To set up importing from a CSV file, follow these steps:
1. Create a GameTable object (right-click in the Project window and choose *Create / Game Tables / Game Table*).
2. Set up the GameTable object properties:
    1. Choose *CSV* in the [Source Type]({{ site.baseurl }}{% link reference/inspector.md %}#source) dropdown.
    2. In the **Asset** field, reference the `.csv` file (a [`TextAsset`](https://docs.unity3d.com/Manual/class-TextAsset.html)) to import from.
    3. In the [Search Path]({{ site.baseurl }}{% link reference/inspector.md %}#search-path) field, enter the path to the folder containing the Prefabs the CSV file references. The path is relative to the project root, for example `Assets/Prefabs/Units`.
    4. Optional. Specify additional settings that alter the way the table data should be interpreted. For example, you can choose whether to use object-per-row or property-per-row orientation. For more, see [GameTable Inspector]({{ site.baseurl }}{% link reference/inspector.md %}).
3. Click [Apply Game Table]({{ site.baseurl }}{% link reference/inspector.md %}#apply-game-table).
4. Check the Console window. If everything went well, it should contain a message like the following:
   > Game Tables: modified 5 objects (of 5), 53 properties (of 88), 0 items removed

   If the Console contains any errors, address them and click *Apply Game Table* again.
5. Optional. Save all the changes made by Game Tables via *File / Save Project*.
