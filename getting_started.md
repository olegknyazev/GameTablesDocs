---
title: Getting Started
nav_order: 1
---
# Getting Started

## Importing Package
After purchasing the package on Asset Store, you can import it into your project via the [Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html). To do so, select *Packages: My Assets* in the Packages dropdown menu, find Game Tables in the list and click Import.

## Example Scene
The Game Tables package contains an example scene showcasing its use. To import this example into your project, find Game Tables in the Package Manager window and click Import on the Samples tab.

This action will add `Samples/Game Tables/<version>/Game Tables Example Project` folder to your project. This folder contains an example scene and all the assets required for it to work. It is completely optional and can be deleted at any time.

The entry point to the showcase is the `Example` scene located at the root of the example folder. If you open this scene and enter Play mode, you'll be able to play a simple top-down shooting game with placeholder graphics. The key point of this example is that all the essential gameplay parameters are stored in spreadsheets.

These spreadsheets are referenced by the `Balance_*` assets which can be found in the example folder. There are four such assets:
* `Balance_Original_CSV` imports from the `CSV/Balance_Original.csv` file
* `Balance_Alternative_CSV` imports from the `CSV/Balance_Alternative.csv` file
* `Balance_Original_GoogleSheets` imports from the [Balance_Original](https://docs.google.com/spreadsheets/d/1xaYudoHmST4hAjno8C70gcSN_2oSyo7w69sZz49FHO4/edit?usp=sharing) Google Sheets document
* `Balance_Alternative_GoogleSheets` imports from the [Balance_Alternative](https://docs.google.com/spreadsheets/d/1HuHCQntTOQbM6wg0M750dN4ybKULCeGTuy6XouFTTWY/edit?usp=sharing) Google Sheets document

`Original` and `Alternative` refer to two different variations of gameplay parameters, whereas `CSV` and `GoogleSheets` refer to different data sources. By default, the Original version of the balance is applied. You can try the Alternative version by selecting either CSV or GoogleSheets asset and clicking *Apply Game Table* in the Inspector.

| If you go with the Google Sheets option, you'll need to authorize Game Tables in Google Sheets before using it. To do so, click Authenticate in the Inspector and follow the instructions in your browser. For further information, see [Authorize in Google Sheets]({{ site.baseurl }}{% link guides/authorize_in_google_sheets.md %}). |

If you want to experiment with this example a bit further, feel free to copy one of the spreadsheets mentioned above, make some changes to it, and point one of the existing Game Tables to your version of the file (or create a brand-new Game Table altogether).

If you want to learn more about the Game Tables workflow and data formats, you may find the [Main Concepts]({{ site.baseurl }}{% link main_concepts.md %}) page useful.

## Package Structure
Game Tables is distributed as a UPM package and is installed into the `Packages/Game Tables` folder. Under this folder, you can find the following:

 * **Editor**
 
   This is the main directory containing the Game Tables source code, which is compiled into the `GameTables.Editor` [assembly](https://docs.unity3d.com/Manual/ScriptCompilationAssemblyDefinitionFiles.html).

 * **ThirdParty**
 
   This directory contains the third-party assemblies required by Game Tables. Here you can also find the `LICENSES.txt` file with licensing information for all the third-party components.

 * **Tests.zip**
   
   This is the test suite for Game Tables, which can be useful if you intend to modify the source code. It's packed into a ZIP archive so that these tests are not processed by Unity and are not displayed in the Test Runner window. If you want to make the Game Tables tests runnable, simply unpack the archive.
