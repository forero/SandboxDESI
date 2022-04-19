import desientropy.sky_sframe

for i in range(15,0,-1):
        print(i)
        desientropy.sky_sframe.summary_entropy_night("daily", 20220400+i, sample_lambda=True)

