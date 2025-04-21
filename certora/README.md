# Certora Formal Verification of Account Abstraction

## Setup
Before running any verification, apply the patches first:
```sh
git apply ./certora/patch/*.patch
```

You can reverse the patches later with:
```sh
git apply -R ./certora/patch/*.patch
```

## Core Stake and Deposit Management & Nonce Verification
Run these configurations to verify core logic of staking, deposits and nonce functionality:

```sh
certoraRun certora/conf/management_quick_rules.conf
certoraRun certora/conf/management_advanced_rules.conf
certoraRun certora/conf/management_no_havoc.conf 
certoraRun certora/conf/nonce.conf
```

- `management.conf` checks most properties on deposits and staking, as well as a few generic rules.
- `management_no_havoc.conf` checks how the core account-abstraction functions (`handleOps` and `handleAggregatedOps`) impact deposits. It uses different summarization compared to other management specs to workaround some havocs.

## EntryPoint Validation & Execution Verification
These configurations verify the critical property stating "Only validated calls are executed, and all of them are executed as a bundle":

- `EntryPoint.conf` and `EntryPoint_sanity.conf` check the property respectively (TBD whether to run sesparately with scripts or not)
- `nonHandleOps.conf` checks this property trivially on all methods in the contract for completeness
- `residual.conf` checks that the summary for `innerHandleOp` used in the main `EntryPoint` confs is correct.


Generating Reports
The report directory contains scripts for running the validation-implies-execution property verification and generating reports.

To run the verification and generate a markdown report:

1. Update the input/output files in markdown.sh:
```sh
# Update these variables as needed
input_file="certora/report/all_sanity.sh"  # Input verification script
output_file="certora_results_sanity.md"    # Output markdown report
```

2. Run the report generation:

```sh
./certora/report/markdown.sh
```

This will execute the verification steps and generate a markdown table with the results.

