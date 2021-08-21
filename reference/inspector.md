---
parent: Reference
title: Inspector
nav_order: 3
---
# Inspector
![Game Tables Inspector UI]({{ site.baseurl }}{% link reference/inspector.png %})

Source
 : Determines type of table data source. Currently CSV files and Google Sheets documents are supported. The following parameters depend on selected value.

Spreadsheet Id
 : An identifier of a Google Sheets document to import. Spreadsheet Id looks like a long sequence of letters and numbers. You may paste the entire URL of an Google Sheets document from the browser address bar—the interesting part will be extracted automatically.

   In order to access Google Sheets documents you need to authorize in Google and grant access for Game Tables application. In case if you have not authorized yet, a special UI will be shown below. More information about Google Sheets authrozation see in **TBD**.

   This property only shown when *Source* is set to *Google Sheets*.

Spreadsheet Name
 : A read-only field that displays the name of the specified Google Sheets document. It helps you be sure that you specified correct *Spreadsheet Id*.

   This property only shown when *Source* is set to *Google Sheets*.

Sheets to Import
 : A checklist that specifies which sheets from a document you want to import. You may use this property for multi-sheets documents to make Game Tables import only some of them.

   This property only shown when *Source* is set to *Google Sheets*.

Orientation
 : Determines how to interpret column and row headers. The default mode is *Object Per Row* in which case row headers are considered as prefab names (with optional property prefixes) and column headers are considered as property names. The *Property Per Row* mode "flips" the table. More on row and columns headers see in [Headers Format]({{ site.baseurl }}{% link reference/headers_format/index.md %}).

Layout
 : Determines whether Game Tables should interpret the whole document as a single table or a collection of multiple tables. Each table has separate row and column headers. So, by using *Islands* mode you may define properties for objects of various types in a single table. The *Single Table* mode supposes that the whole table has a single heading row and heading column.

   For multisheet documents (i.e. Google Sheets) this property is applied to each sheet. That is, you may have several sheets in a document and each of these sheets may contain several tables.

   To make part of a table an island, separate it from surroundings by a border of empty cells.

Search Path
 : Specifies the root folder for searching assets that are referenced in table. This folder is used for both target prefabs and referenced prefabs.