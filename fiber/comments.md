
1. In the introduction. "there will be a similar issue, caused by limitations in the placement of fibers close to each other".  
    This is imprecise. The issue is the collision of the positioners that could happen even if the fibers are far from each other.  
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
    



