# copyIngest

***Work In Progress***

Copies files from a source location to a destination location, preserving file structure and formatting it by date.

## How to use

1. Clone repo `git clone https://github.com/garrettsummerfi3ld/copyIngest.git`
2. Enter repo `cd copyIngest`
3. Modify `vars.json` to your personal liking, with source and destination paths, and even file types
4. `pip -m install requirements.txt`
5. `python copyIngest.py`

## How to set up custom variables

```json
{
    "sourcePath" : "",
    "destPath" : "",
    "allowFileTypes" : [
        ""
    ]
}
```
