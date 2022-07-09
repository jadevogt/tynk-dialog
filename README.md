# Tynk Dialog Tool
[![Test Core Functionality](https://github.com/jadevogt/tynk-dialog/actions/workflows/test_core_functionality.yml/badge.svg)](https://github.com/jadevogt/tynk-dialog/actions/workflows/test_core_functionality.yml)

## Overview
This is an early development version of a tool that can be used to create, edit, and eventually preview dialog boxes for the upcoming game [Tynk! and the Final Phonorecord](https://tynkga.me/). 

## Roadmap
- Proof of Concept
  * Open dialog files saved in the JSON based file format
  * Edit the content and settings of the dialog files interactively
  * Serialize the edited content back into the JSON format so it can be used in the game engine
- Basic Functionality
  * Fully featured command line interface
  * Support for the game engine's light markup language features
    - Text colors
    - Behaviors (text effects)
    - Print delay
- Game File Integration
  * Automatically pull data from a configured game data path in the filesystem
  * Check user input against the character, blip, textbox style info found in the game files
  * Support opening / editing / saving content directly to and from the game files
- Basic Graphical User Interface
  * Implement a Qt UI with PySide6
  * Provide familiar editing idioms (File Edit View etc.)
  * Provide dropdown menus for game data pulled from other files
- Advanced Functionality
  * Rich text editing inside the dialog tool interface
  * Preview sound blips
  * Preview text colors and animations
  * Drag and drop capability for rearranging dialog
  * Preview dialog in styled textbox without opening GameMaker?
