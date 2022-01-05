---
title: Getting Started
nav_order: 2
---
# Getting Started

## Importing Package
After purchasing the package on Asset Store, you can import it into your project via [Project Manager window](https://docs.unity3d.com/Manual/upm-ui.html). To see your Asset Store package select *Packages: My Assets* in the Packages dropdown menu.

## Package Structure
By default Game Tables package is located in `Assets/GameTables` directory. This directory has the following structure:

 * **Example**
 
   This directory contains a showcase example. It contains all the content used in the example, including scripts, prefabs, tables and a demo scene. The Example directory may be freely removed from the project, it does not affect Game Tables functioning. For more information on the example see the [Example](#example) section below.

 * **Scripts**
 
   This directory contains Game Tables code. All the code is put into a separate assembly to speed up compilation process.

 * **ThirdParty**
 
    This directory contains third-party assemblies required by Game Tables. Here you also may find `LICENSES.txt` file that contains licensing information on all the used third-parties.

## Example
Game Tables package contains a showcase example that shows you a (pretty simplified) way of how Game Tables may be used in game creation.

The entry point to showcase is the Example scene that resides at the Example folder root. If you open this scene and run the play mode, you'll see a simple top-down shooting game with blocking graphics. The key point is that all the essential gameplay parameters of this game are stored in ScriptableObjects and Prefab which, in turn, get these values from spreadsheets. And there are two variants of game balance that may be easily applied to see changes in action.

In the Example folder you may see a set of assets whose names start from `Balance_`. These assets are GameTable objects, each of which is set up to import data from a specific table:
* `Balance_Original_CSV` imports from the `CSV/Balance_Original.csv` file
* `Balance_Alternative_CSV` imports from the `CSV/Balance_Alternative.csv` file
* `Balance_Original_GoogleSheets` imports from the [Balance_Original](https://docs.google.com/spreadsheets/d/1xaYudoHmST4hAjno8C70gcSN_2oSyo7w69sZz49FHO4/edit?usp=sharing) Google Sheets document
* `Balance_Alternative_GoogleSheets` imports from the [Balance_Alternative](https://docs.google.com/spreadsheets/d/1HuHCQntTOQbM6wg0M750dN4ybKULCeGTuy6XouFTTWY/edit?usp=sharing) Google Sheets document

By default the example has the Original balance variant applied. You may open either a CSV or GoogleSheets version with Alternative balance variant and click the *Apply Game Table* button in the Inspector. Then run the game again and see how the gameplay is changed.
