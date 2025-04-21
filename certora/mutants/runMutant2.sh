git apply ./certora/patch/prover_optimization.patch 
git apply ./certora/mutants/mutant2.patch 

certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps110_mutant2 --rule onlyValidatedCalls_3HandleAggregatedOps110

git apply -R ./certora/mutants/mutant2.patch
git apply -R ./certora/patch/prover_optimization.patch 

