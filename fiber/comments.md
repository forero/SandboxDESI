
0. In October 2017 we fixed a bug that made that unfibered targets followed a pattern on the focal plane.
    This was due to a cycle on the positioner index that always followed the same order for every tile. Now this cycle is different
    for every tile. So, there was an additional reason for zero-probability pairs besides tiling. 
    See the details here: https://github.com/desihub/fiberassign/pull/84 
    Please write down somewhere the version of `fiberassign` that you used. This will be useful internal to the collaboration to 
    remember/reconstruct what bugs were still present in the version you used.   

1. In the introduction. "there will be a similar issue, caused by limitations in the placement of fibers close to each other".  
    This is imprecise. The issue is the collision of the positioners. That could happen even if the fibers are far from each other.  
    See Cell 12 for an example of positioner collision where the fibers are far apart https://github.com/forero/SandboxDESI/blob/master/fiber/PositionerShape.ipynb . 
    `fiberassign` explicitly has to check for the positioner shapes to avoid collisions, not only distances between fibers.
    
2. In Section 2. It should also be mentioned that an ELG can remain witout a fiber because there are two more classes of targets (LRG, QSO) in competition for the fibers. This is implicit in Table 1, but is not explicitly mentioned that the efficiency depends on the 
local density of all three galaxy types LRG, QSO, ELG. This mentioned in Section 4 and 5, but it should also be mentioned earlier, 
it's not clear at the end of Section 4 why are you suddenly talking about "picking quasars".

3. In Section 3. "when the targeting algorithm is run".  
    Shouldn't this be instead "the fibre assignment algorithm"?  
    In many places in the text apears "targeting" when it actually means "fibre assignment". 
    
4. In Section 3.  
    What changes in the "N_bits" different runs? `fiberassign` is deterministic. Do you change the `subpriorities` for each ELG?
    This should be clarified in the text.

5. In Section 4.  
    `fiberassign` is not stochastic anymore. The randomness will enter through the `subpriorities` does that change your conclusions regarding DESI?
    


