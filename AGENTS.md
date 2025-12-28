# AGENTS.md

Guidelines for AI agents and contributors working on this repository.

## Project Overview

**Title:** *Undergraduate Mathematics: From the Top*

**Type:** Comprehensive undergraduate mathematics textbook

**Author:** Robert Jackson

**Started:** 2009

## Content Scope

This textbook covers the following subjects:

1. **Calculus I–III** — Calculus I is complete
2. **Statistics**
3. **Statics**
4. **Discrete Mathematics**
5. **Differential Equations**
6. **Linear Algebra**

## Target Audience

All content should be written with non-traditional students in mind:

- Returning learners who may have been away from formal education
- Working adults balancing school with employment and family
- Students seeking a fresh, accessible approach to mathematics

**Tone:** Approachable, clear, and supportive. Avoid assumptions about prior knowledge. Build concepts from foundational principles.

## License Information

**Undergraduate Mathematics: From the Top © 2009 by Robert Jackson is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/**

### What This Means

- **Attribution (BY):** Credit must be given to the author
- **NonCommercial (NC):** Others may not use this work commercially
- **ShareAlike (SA):** Adaptations must use the same license

The author retains full commercial rights to produce and sell physical and digital copies.

## Contribution Guidelines

When contributing or making modifications:

1. Maintain the approachable, accessible tone suitable for non-traditional students
2. Ensure mathematical accuracy and clarity
3. Include examples that relate to real-world applications where possible
4. Respect the CC BY-NC-SA 4.0 license terms
5. Provide proper attribution for any adapted content
6. Do not use emoji unless explicitly requested

## Coding Standards

All code in this repository must adhere to the following standards:

### General Requirements

- All linting errors must be resolved before committing code
- Code must pass both Pylint and Pylance validation

### Python Standards

1. **Main Function Required:** All Python scripts must use a `main()` function with the standard entry point pattern:
   ```python
   def main() -> None:
       '''
       Main entry point.
       '''
       # code here

   if __name__ == "__main__":
       main()
   ```

2. **Docstrings Required:** All modules, classes, and functions must have docstrings following Google or NumPy style. Use multi-line format with single quotes:
   ```python
   def foo() -> None:
       '''
       Brief description of what the function does.
       '''
       pass
   ```

3. **Type Hints Required:** All function parameters and return values must have type annotations. This is not optional.

4. **Linting:** All Python code must be validated with:
   - Pylint (resolve all errors and warnings)
   - Pylance (resolve all reported issues)
