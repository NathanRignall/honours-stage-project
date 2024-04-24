# Live Software Updates in a Real-Time System 

## Report

This folder contains the final report. Written in LaTeX, it can be compiled using the following command:

Make graphics & report:
```bash
make all
```

Make report:
```bash
make thesis.pdf
```

## Elafry

This is the codebase for the developed software infrastructure, codenamed Elafry.

It contains two main components:
1. Elafry - The main library for the Elafry software infrastructure.
2. Apps - The applications that use the Elafry library.

This can be compiled using the following command:

```bash
cargo build --release
```

## Data Test

This folder contains all the test programs used to test scheduling methods.