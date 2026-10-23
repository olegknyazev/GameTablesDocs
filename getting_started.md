---
title: Getting Started
nav_order: 1
---
# Getting Started

## Importing the Package
After purchasing the package on the Asset Store, you can import it into your project via the [Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html). To do so, select *Packages: My Assets* in the Packages dropdown menu, find Game Tables in the list, and click *Import*.

## Example Scene
The Game Tables package contains an example scene that demonstrates a typical setup. To import this example into your project, find Game Tables in the Package Manager window and click *Import* on the Samples tab.

| The example uses the [Universal Render Pipeline (URP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@14.0/manual/index.html). If your project uses a different render pipeline, import the example into a separate project created from Unity's URP template. |

This adds the `Samples/Game Tables/<version>/Game Tables Example Project` folder to your project, containing the scene and all the supporting assets. It is completely optional and can be deleted at any time.

The example's entry point is the `Example` scene at the root of that folder. If you open this scene and enter Play mode, you can play a simple top-down shooter with placeholder graphics. The key point of this example is that all the essential gameplay parameters are stored in spreadsheets.

Four `Balance_*` assets in the example folder reference these spreadsheets:
* `Balance_Original_CSV` imports from the `CSV/Balance_Original.csv` file
* `Balance_Alternative_CSV` imports from the `CSV/Balance_Alternative.csv` file
* `Balance_Original_GoogleSheets` imports from the [`Balance_Original`](https://docs.google.com/spreadsheets/d/1xaYudoHmST4hAjno8C70gcSN_2oSyo7w69sZz49FHO4/edit?usp=sharing) Google Sheets document
* `Balance_Alternative_GoogleSheets` imports from the [`Balance_Alternative`](https://docs.google.com/spreadsheets/d/1HuHCQntTOQbM6wg0M750dN4ybKULCeGTuy6XouFTTWY/edit?usp=sharing) Google Sheets document

`Original` and `Alternative` are the two variations of gameplay parameters, whereas `CSV` and `GoogleSheets` are the two data source types. By default, the `Original` version is applied. You can try the `Alternative` version by selecting either the `CSV` or the `GoogleSheets` asset and clicking *Apply Game Table* in the Inspector.

| If you go with the Google Sheets option, you'll need to sign in to your Google account first. Click *Sign In* in the Inspector and follow the instructions in your browser. For more, see [Sign In to Google Sheets]({{ site.baseurl }}{% link guides/sign_in_to_google_sheets.md %}). |

If you want to experiment with this example further, feel free to copy one of the spreadsheets above, edit it, and point one of the existing GameTables at your copy (or create a new GameTable from scratch).

When you're ready to go beyond the example, the [Main Concepts]({{ site.baseurl }}{% link main_concepts.md %}) page covers the Game Tables workflow and data formats.

## Package Structure
Game Tables is distributed as a UPM package and is installed into the `Packages/Game Tables` folder. Inside, you'll find:

 * `Editor`
 
   Game Tables source code, compiled into the `GameTables.Editor` [assembly](https://docs.unity3d.com/Manual/ScriptCompilationAssemblyDefinitionFiles.html).

 * `ThirdParty`
 
   Third-party assemblies required by Game Tables.

 * `Third-Party Notices.txt`
 
   Licensing information for the third-party assemblies.

 * `Tests.unitypackage`
   
   The test suite, useful if you intend to modify the source code. It's packed into a separate package so the tests aren't processed by Unity or shown in the Test Runner window. Import it into your project to make them runnable.
