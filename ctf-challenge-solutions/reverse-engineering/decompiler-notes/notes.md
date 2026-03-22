# Decompiler Usage Notes & Tricks

## Ghidra
1. **Auto-Analysis Profile**: Upon loading a new binary, always allow Ghidra to auto-analyze using the default set. Sometimes, checking "Decompiler Parameter ID" provides clearer function signatures.
2. **Renaming Variables**: The `L` key is your friend. Press `L` while highlighting a variable in the pseudocode to rename it across the entire function block.
3. **Change Variable Types**: Press `Ctrl+L` or right-click to change the auto-detected data type. A `char *` looks very different structurally than `int[]`.
4. **Export to C**: You can export the decompiled source as a C file to perform static analysis outside of the GUI.

## IDA Free
1. **Graph View mode**: Hit `Space` while in text mode to switch to Graph View. This shows the code branches (red=false, green=true) and helps visually map logic jumps quickly.
2. **String References**: `Shift+F12` opens the strings window. Double-click a suspicious string, then press `x` on its label to cross-reference and jump directly to the code where the string is used (often right next to a comparison function).
3. **F5 Pseudocode**: In IDA Pro (and modern Free versions depending on the architecture), `F5` generates high-level C-like pseudocode.

## Best Practices in Reversing
- Start at `main()`, not just the binary entry point `_start`.
- Follow the prompt strings: if an app asks for a password via "Enter key: ", cross-referencing that string usually immediately leads you to the validation function.
- Be cautious of compiler optimization traps. Sometimes loops or math operations are unrolled/optimized into bitwise operations that look confusing manually but are standard compiler routines.
