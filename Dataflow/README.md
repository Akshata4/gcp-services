## CODE
Here’s a minimal Python example that:

Reads the input file

Splits each line by comma

Filters records where age > 40

Writes the output to a text file

## INPUT FILE
Each line represents a record (e.g., name, age, country).

## Summary Table: Key Steps

| Step       | Tool/Transform       | Purpose                                  |
|------------|----------------------|------------------------------------------|
| Input File | Plain text (CSV)     | Source data for pipeline                  |
| Read       | ReadFromText         | Load lines from file into PCollection    |
| Transform  | ParDo, Filter, Map   | Split, filter, and format records        |
| Output     | WriteToText          | Write processed data to output file       |
