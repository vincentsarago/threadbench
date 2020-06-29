# threadbench

Benchmark rio-tiler in multithreading

### CircleCI - 4 Go/2 CPU

#### 1 image
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |  **294.1420** (1.0)  |   **404.5836** (1.0)  | **319.4468** (1.0)  | **299.5392** (1.0)    
1  |  807.0299 (2.74) |   925.4274 (2.29) | 876.3400 (2.74) | 892.5641 (2.98)   
2  |  819.5475 (2.79) | 1,022.1908 (2.53) | 940.3364 (2.94) | 964.6628 (3.22)   
5  |  853.0657 (2.90) |   997.8313 (2.47) | 903.8755 (2.83) | 884.4158 (2.95)   
10 |  869.6996 (2.96) |   950.6192 (2.35) | 908.2337 (2.84) | 905.9879 (3.02)   
------------------------------------------------------------------------------------------------------

#### 2 images
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |    **549.1481** (1.0)  |   **630.4673** (1.0)  |   **569.5167** (1.0)  |   **556.5279** (1.0)    
1  |  1,199.5295 (2.18) | 1,381.2332 (2.19) | 1,275.5596 (2.24) | 1,272.1273 (2.29)   
2  |    877.8752 (1.60) |   974.2414 (1.55) |   922.8445 (1.62) |   927.3491 (1.67)   
5  |    865.3814 (1.58) | 1,066.1524 (1.69) |   967.3984 (1.70) |   971.4911 (1.75)   
10 |    881.8814 (1.61) |   963.2336 (1.53) |   931.5850 (1.64) |   940.5658 (1.69)   
------------------------------------------------------------------------------------------------------------

#### 5 images
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |  1,484.2492 (1.58) | 1,753.7601 (1.73) | 1,554.3400 (1.58) | 1,501.9270 (1.52)   
1  |  2,012.5353 (2.14) | 2,220.2080 (2.19) | 2,153.5138 (2.18) | 2,192.6766 (2.22)   
2  |  1,460.7138 (1.56) | 1,623.8741 (1.60) | 1,569.3857 (1.59) | 1,578.5268 (1.60)   
5  |    983.3246 (1.05) | 1,013.2483 (1.0)  | 1,001.1378 (1.02) | 1,006.1979 (1.02)   
10 |    **939.2216** (1.0)  | **1,021.2605** (1.01) |   **985.9975** (1.0)  |   **986.9281** (1.0)    
------------------------------------------------------------------------------------------------------------

#### 10 images
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |  2,741.0271 (2.89) | 3,791.7001 (3.05) | 3,201.1527 (3.03) | 3,037.6727 (2.96)   
1  |  3,435.9542 (3.62) | 3,824.1275 (3.08) | 3,556.6640 (3.36) | 3,499.0770 (3.41)   
2  |  2,019.7676 (2.13) | 2,290.2476 (1.84) | 2,144.9603 (2.03) | 2,154.8723 (2.10)   
5  |  1,246.1342 (1.31) | 1,379.1334 (1.11) | 1,290.7816 (1.22) | 1,258.8304 (1.23)   
10 |   **948.6572** (1.0)  | **1,243.0330** (1.0)  | **1,057.3221** (1.0)  | **1,026.4667** (1.0)    

### Lambda - 3008Mo

#### 1 image
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0 | **319.5311**  (1.0) | **412.6792**  (1.0) | **339.8609** (1.0) | **322.3923**  (1.0)
1 |  1,210.6804 (3.79) | 1,301.9578 (3.15) | 1,241.6913 (3.65) | 1,234.0741 (3.83)
2 | 1,172.1612 (3.67) | 1,348.2320 (3.27) | 1,240.4083 (3.65) | 1,232.0792 (3.82)
5 | 1,151.6205 (3.60) | 1,250.5128 (3.03) | 1,193.5694 (3.51) | 1,195.8773 (3.71)
10 | 1,164.5260 (3.64) | 1,317.2704 (3.19) | 1,235.0513 (3.63) | 1,218.6710 (3.78)

#### 2 images
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0 | **623.7841**  (1.0) | **725.9318**  (1.0) | **647.4710**  (1.0) | **624.0453**  (1.0)
1 | 1,617.8032 (2.59) | 1,922.3259 (2.65) | 1,737.5530 (2.68) | 1,711.4968 (2.74)
2  | 1,282.6847 (2.06) | 1,430.8142 (1.97) | 1,333.2005 (2.06) | 1,311.4794 (2.10)
5  | 1,212.3974 (1.94) | 1,448.6309 (2.00) | 1,339.5890 (2.07) | 1,327.7736 (2.13)
10 | 1,299.6578 (2.08) | 1,366.2074 (1.88) | 1,323.3048 (2.04) | 1,315.1479 (2.11)

#### 5 images
Threads | Min (s) | Max (s) | Mean (s) | Median (s)
--- | --- | --- | --- | ---
0  | **1.5098**  (1.0) | 1.8823 (1.09) | **1.6113**  (1.0) | **1.5512**  (1.0)
1  | 2.9100 (1.93) | 3.1608 (1.83) | 3.0085 (1.87) | 2.9661 (1.91)
2  | 2.0596 (1.36) | 2.2160 (1.28) | 2.1221 (1.32) | 2.0805 (1.34)
5  | 1.6186 (1.07) | 1.7390 (1.01) | 1.6662 (1.03) | 1.6612 (1.07)
10 | 1.6229 (1.07) | **1.7276**  (1.0) | 1.6689 (1.04) | 1.6626 (1.07)

#### 10 images
Threads | Min (s) | Max (s) | Mean (s) | Median (s)
--- | --- | --- | --- | ---
0  | 2.9854 (1.40) | 3.7155 (1.61) | 3.2693 (1.45) | 3.1288 (1.37)
1  | 4.7636 (2.23) | 5.2010 (2.25) | 5.0508 (2.24) | 5.1104 (2.24)
2  | 3.1438 (1.47) | 3.3817 (1.46) | 3.2501 (1.44) | 3.2884 (1.44)
5  | 2.3656 (1.11) | 2.4647 (1.07) | 2.4045 (1.07) | 2.4096 (1.06)
10 | **2.1382** (1.0) | **2.3116**  (1.0) | **2.2519**  (1.0) |  **2.2773** (1.0) 
------------------------------------------------------------------------------------------------------------

### Lambda - 1024Mo

#### 1 image
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |  **342.4245** (1.0) | **440.7617** (1.0)  | **366.9072** (1.0) | **354.0303** (1.0)  
1  | 1,185.4102 (3.46) | 1,680.4160 (3.81) | 1,411.4264 (3.85)|  1,378.2750 (3.89)
2  | 1,276.0163 (3.73) | 1,402.6163 (3.18) | 1,363.2389 (3.72)|  1,377.5307 (3.89)
5  | 1,276.7635 (3.73) | 1,406.4971 (3.19) | 1,334.7448 (3.64)|  1,310.9438 (3.70)
10 | 1,160.0332 (3.39) | 1,452.6234 (3.30) | 1,293.9029 (3.53)| 1,247.5131 (3.52)

#### 2 images
Threads | Min (ms) | Max (ms) | Mean (ms) | Median (ms)
--- | --- | --- | --- | ---
0  |   **699.7538** (1.0)  |  **918.3390** (1.0) | **771.4156** (1.0)  | **722.3720**(1.0) 
1  | 1,739.3016 (2.49) | 2,170.9987 (2.36) | 1,957.4960 (2.54) | 1,949.9554 (2.70)
2  | 1,323.1748 (1.89) | 1,696.3618 (1.85) | 1,571.4674 (2.04) | 1,629.1423 (2.26)
5  | 1,539.2294 (2.20) | 1,622.2178 (1.77) | 1,595.3772 (2.07) | 1,600.0605 (2.22)
10 | 1,458.2745 (2.08) | 1,695.3427 (1.85) | 1,559.7452 (2.02) | 1,560.1526 (2.16)

#### 5 images
Threads | Min (s) | Max (s) | Mean (s) | Median (s)
--- | --- | --- | --- | ---
0  |  **1.7280** (1.0)  | **1.8608** (1.0)  | **1.8204**  (1.0) | **1.8532** (1.0) 
1  |  3.4864 (2.02) | 3.9305 (2.11) | 3.6914 (2.03) | 3.6653 (1.98)
2  |  2.4872 (1.44) | 2.7892 (1.50) | 2.6252 (1.44) | 2.5966 (1.40)
5  |  2.1542 (1.25) | 2.5183 (1.35) | 2.3007 (1.26) | 2.2236 (1.20)
10 |  2.2286 (1.29) | 2.5157 (1.35) | 2.3644 (1.30) | 2.3276 (1.26)

#### 10 images
Threads | Min (s) | Max (s) | Mean (s) | Median (s)
--- | --- | --- | --- | ---
0  | 3.6784 (1.03) | 4.2796 (1.08) | 3.9639 (1.07) | 3.9597 (1.09)
1  | 6.0289 (1.69) | 6.6111 (1.67) | 6.2838 (1.70) | 6.2999 (1.74)
2  | 4.1351 (1.16) | 4.5220 (1.14) | 4.3533 (1.18) | 4.4261 (1.22)
5  | 3.7647 (1.06) | 4.0384 (1.02) | 3.9429 (1.07) | 3.9959 (1.10) 
10 | **3.5582** (1.0) | **3.9652** (1.0)  | **3.6913** (1.0)  | **3.6214** (1.0) 
