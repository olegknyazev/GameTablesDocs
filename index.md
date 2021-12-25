---
title: About
nav_order: 0
---
# About
Game Tables is a Unity plugin for importing prefab properties from tables. It works with online Google Sheets documents and local CSV files.

## Why Would I Need It?
Unity has a powerful editor that allows you enter data right into the Prefabs, ScriptableObjects and objects in the scene. It's very convenient and saves a lot of programming effort on writing serialization machinery.

But Unity editor may not work well for some kinds of data used in games. Suppose that you develop a game in which you have several upgrades that the player may purchase. And you need to balance them. It may be too cumbersome to do this by setting properties in Inspector. Professional game designers often use spreadsheets for these tasks: Excel, Google Sheets, etc. With using such tools you may enter a formula and get the values for all the upgrade levels at once. And you may enter another formula and infer how much time it would take to kill an enemy at each upgrade level. With a time-tested and well-known tool you optimise the development efforts and do not spend time in reinventing required functionally in your custom editor extensions.

Game Tables builds a bridge between Unity editor and spreadsheets. It imports object properties from tables and applies them to Prefabs and ScriptableObjects in your project. Game Tables is *made for designers* and it *does not require any coding* to use it.
