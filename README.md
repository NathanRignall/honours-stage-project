# honours-stage-project

## Report

This folder contains the final report for the project. Written in LaTeX, it can be compiled using the following command:

Make graphics & report:
```bash
make all
```

Make report:
```bash
make thesis.pdf
```

## [Elafry](elafry)

This is the codebase for the developed software infrastructure, codenamed Elafry.

It contains two main components:
1. [Elafry](elafry/crates) - The main library for the Elafry software infrastructure.
2. [Apps](elafry/apps) - The applications that use the Elafry library.

This can be compiled using the following command:

```bash
cargo build --release
```

## Data Test

This folder contains all the test programs used to test scheduling methods.