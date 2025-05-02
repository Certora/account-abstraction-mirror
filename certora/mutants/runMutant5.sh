git apply ./certora/mutants/mutant5.patch # includes prover_optimization.patch

certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleOps_mutant5 --rule onlyValidatedCalls_1HandleOps

git apply -R ./certora/mutants/mutant5.patch
