git apply ./certora/mutants/mutant6.patch # includes prover_optimization.patch

certoraRun certora/conf/EntryPointOrderExecution.conf --build_cache --server prover --msg iterationOrder_mutant6 --rule iterationOrder_HandleOps

git apply -R ./certora/mutants/mutant6.patch
