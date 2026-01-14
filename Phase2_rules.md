# Phase 2 – Rule-Based Validation

## Purpose
Phase 2 validates the cleaned clinical dataset against explicitly defined
structural and variable-level rules. The goal is to determine whether the
dataset conforms to expected standards before further analysis.

## Dataset Scope
- Input: Cleaned dataset produced from Phase 1
- Scope: Structural and variable-level validation
- Excludes: Full CDISC SDTM compliance and ADaM derivations

## Critical Variables
The following variables are considered critical for validation:
- SUBJECT_ID
- AGE
- SEX
- VISIT_DATE
- STATUS

## Structural Rules
- All critical variables must exist as columns in the dataset
- Column names must match expected naming conventions
- No duplicate column definitions are allowed

## Variable-Level Rules

### SUBJECT_ID
- Must exist
- Must not be null
- Must be unique across records

### AGE
- Must be numeric
- Must be between 0 and 120

### SEX
- Must not be null
- Must be one of: M, F

### VISIT_DATE
- Must exist
- Must follow valid date format

### STATUS
- Must not be null
- Must belong to a predefined set of allowed values

## Rule Severity
- Critical: Violations that invalidate a record or dataset
- Warning: Violations that require attention but do not block processing

## Expected Output
- Record-level validation status (PASS / FAIL)
- Summary of rule violations by variable and severity
