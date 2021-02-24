# Prompt String 1

### Change the primary prompt string to a custom string.

------

## Install:
Append this in your `.bashrc`, `.profile` or `.bash_aliases` :

```bash
ps1 () { eval \`python ps1 $@\`; }

```

## Usage:
```bash
# Change to "Front$ " colored green and white.
ps1 GREENFrontWHITE$

# Change to "Backend >> " colored red and black.
ps1 %RBackend %W>>
```

## Requires:
- Python 3^ (Tested with 3.8.2)