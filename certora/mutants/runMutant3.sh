git apply ./certora/patch/prover_optimization.patch 
git apply ./certora/mutants/mutant3.patch 

certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps002_mutant3 --rule onlyValidatedCalls_3HandleAggregatedOps002

git apply -R ./certora/mutants/mutant3.patch
git apply -R ./certora/patch/prover_optimization.patch 

