
git apply ./certora/patch/prover_optimization.patch 
git apply ./certora/mutants/mutant1.patch 

certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleOps_mutant1 --rule onlyValidatedCalls_2HandleOps

git apply -R ./certora/mutants/mutant1.patch
git apply -R ./certora/patch/prover_optimization.patch 

