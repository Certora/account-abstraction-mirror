git apply ./certora/patch/prover_optimization.patch 
git apply ./certora/mutants/mutant4.patch 

certoraRun certora/conf/EntryPoint_sanity.conf --build_cache --server prover --msg sanity_onlyValidatedCalls_3HandleAggregatedOps001_mutant4 --rule sanity_onlyValidatedCalls_3HandleAggregatedOps001

git apply -R ./certora/mutants/mutant4.patch
git apply -R ./certora/patch/prover_optimization.patch 

