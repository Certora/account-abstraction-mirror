git apply ./certora/patch/prover_optimization.patch 

certoraRun certora/conf/nonHandleOps.conf --build_cache --server prover --msg onlyValidatedCalls_NonHandleOps --rule onlyValidatedCalls_NonHandleOps --parametric_contracts EntryPoint
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleOps --rule onlyValidatedCalls_3HandleOps
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleOps --rule onlyValidatedCalls_2HandleOps
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleOps --rule onlyValidatedCalls_1HandleOps
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_0HandleOps --rule onlyValidatedCalls_0HandleOps
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps000 --rule onlyValidatedCalls_3HandleAggregatedOps000
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps001 --rule onlyValidatedCalls_3HandleAggregatedOps001
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps002 --rule onlyValidatedCalls_3HandleAggregatedOps002
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps003 --rule onlyValidatedCalls_3HandleAggregatedOps003
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps010 --rule onlyValidatedCalls_3HandleAggregatedOps010
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps011 --rule onlyValidatedCalls_3HandleAggregatedOps011
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps012 --rule onlyValidatedCalls_3HandleAggregatedOps012
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps013 --rule onlyValidatedCalls_3HandleAggregatedOps013
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps020 --rule onlyValidatedCalls_3HandleAggregatedOps020
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps021 --rule onlyValidatedCalls_3HandleAggregatedOps021
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps022 --rule onlyValidatedCalls_3HandleAggregatedOps022
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps023 --rule onlyValidatedCalls_3HandleAggregatedOps023
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps030 --rule onlyValidatedCalls_3HandleAggregatedOps030
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps031 --rule onlyValidatedCalls_3HandleAggregatedOps031
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps032 --rule onlyValidatedCalls_3HandleAggregatedOps032
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps033 --rule onlyValidatedCalls_3HandleAggregatedOps033 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps100 --rule onlyValidatedCalls_3HandleAggregatedOps100
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps101 --rule onlyValidatedCalls_3HandleAggregatedOps101
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps102 --rule onlyValidatedCalls_3HandleAggregatedOps102
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps103 --rule onlyValidatedCalls_3HandleAggregatedOps103
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps110 --rule onlyValidatedCalls_3HandleAggregatedOps110
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps111 --rule onlyValidatedCalls_3HandleAggregatedOps111
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps112 --rule onlyValidatedCalls_3HandleAggregatedOps112
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps113 --rule onlyValidatedCalls_3HandleAggregatedOps113
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps120 --rule onlyValidatedCalls_3HandleAggregatedOps120
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps121 --rule onlyValidatedCalls_3HandleAggregatedOps121
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps122 --rule onlyValidatedCalls_3HandleAggregatedOps122
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps123 --rule onlyValidatedCalls_3HandleAggregatedOps123 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps130 --rule onlyValidatedCalls_3HandleAggregatedOps130
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps131 --rule onlyValidatedCalls_3HandleAggregatedOps131
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps132 --rule onlyValidatedCalls_3HandleAggregatedOps132 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps133 --rule onlyValidatedCalls_3HandleAggregatedOps133 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps200 --rule onlyValidatedCalls_3HandleAggregatedOps200
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps201 --rule onlyValidatedCalls_3HandleAggregatedOps201
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps202 --rule onlyValidatedCalls_3HandleAggregatedOps202
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps203 --rule onlyValidatedCalls_3HandleAggregatedOps203
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps210 --rule onlyValidatedCalls_3HandleAggregatedOps210
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps211 --rule onlyValidatedCalls_3HandleAggregatedOps211
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps212 --rule onlyValidatedCalls_3HandleAggregatedOps212
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps213 --rule onlyValidatedCalls_3HandleAggregatedOps213 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps220 --rule onlyValidatedCalls_3HandleAggregatedOps220
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps221 --rule onlyValidatedCalls_3HandleAggregatedOps221
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps222 --rule onlyValidatedCalls_3HandleAggregatedOps222 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps223 --rule onlyValidatedCalls_3HandleAggregatedOps223 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps230 --rule onlyValidatedCalls_3HandleAggregatedOps230
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps231 --rule onlyValidatedCalls_3HandleAggregatedOps231 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps232 --rule onlyValidatedCalls_3HandleAggregatedOps232 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps233 --rule onlyValidatedCalls_3HandleAggregatedOps233 --loop_iter 7
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps300 --rule onlyValidatedCalls_3HandleAggregatedOps300
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps301 --rule onlyValidatedCalls_3HandleAggregatedOps301
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps302 --rule onlyValidatedCalls_3HandleAggregatedOps302
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps303 --rule onlyValidatedCalls_3HandleAggregatedOps303 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps310 --rule onlyValidatedCalls_3HandleAggregatedOps310
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps311 --rule onlyValidatedCalls_3HandleAggregatedOps311
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps312 --rule onlyValidatedCalls_3HandleAggregatedOps312 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps313 --rule onlyValidatedCalls_3HandleAggregatedOps313 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps320 --rule onlyValidatedCalls_3HandleAggregatedOps320
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps321 --rule onlyValidatedCalls_3HandleAggregatedOps321 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps322 --rule onlyValidatedCalls_3HandleAggregatedOps322 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps323 --rule onlyValidatedCalls_3HandleAggregatedOps323 --loop_iter 7
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps330 --rule onlyValidatedCalls_3HandleAggregatedOps330 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps331 --rule onlyValidatedCalls_3HandleAggregatedOps331 --loop_iter 6
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps332 --rule onlyValidatedCalls_3HandleAggregatedOps332 --loop_iter 7
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_3HandleAggregatedOps333 --rule onlyValidatedCalls_3HandleAggregatedOps333 --loop_iter 8
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps00 --rule onlyValidatedCalls_2HandleAggregatedOps00
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps01 --rule onlyValidatedCalls_2HandleAggregatedOps01
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps02 --rule onlyValidatedCalls_2HandleAggregatedOps02
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps03 --rule onlyValidatedCalls_2HandleAggregatedOps03
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps10 --rule onlyValidatedCalls_2HandleAggregatedOps10
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps11 --rule onlyValidatedCalls_2HandleAggregatedOps11
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps12 --rule onlyValidatedCalls_2HandleAggregatedOps12
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps13 --rule onlyValidatedCalls_2HandleAggregatedOps13
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps20 --rule onlyValidatedCalls_2HandleAggregatedOps20
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps21 --rule onlyValidatedCalls_2HandleAggregatedOps21
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps22 --rule onlyValidatedCalls_2HandleAggregatedOps22
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps23 --rule onlyValidatedCalls_2HandleAggregatedOps23
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps30 --rule onlyValidatedCalls_2HandleAggregatedOps30
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps31 --rule onlyValidatedCalls_2HandleAggregatedOps31
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps32 --rule onlyValidatedCalls_2HandleAggregatedOps32
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_2HandleAggregatedOps33 --rule onlyValidatedCalls_2HandleAggregatedOps33 --loop_iter 5
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleAggregatedOps0 --rule onlyValidatedCalls_1HandleAggregatedOps0
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleAggregatedOps1 --rule onlyValidatedCalls_1HandleAggregatedOps1
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleAggregatedOps2 --rule onlyValidatedCalls_1HandleAggregatedOps2
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_1HandleAggregatedOps3 --rule onlyValidatedCalls_1HandleAggregatedOps3
certoraRun certora/conf/EntryPoint.conf --build_cache --server prover --msg onlyValidatedCalls_0HandleAggregatedOps --rule onlyValidatedCalls_0HandleAggregatedOps

git apply -R ./certora/patch/prover_optimization.patch 