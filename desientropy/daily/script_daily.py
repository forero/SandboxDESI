import desientropy.redrock as redrock_entrop
import desientropy.raw_exp
import desientropy.sky_sframe

for month in [9,10]:
    for day in range(0,31):
        desientropy.redrock.summary_release_entropy("daily", lastnight=2022*10000 + month*100 + day)
        #desientropy.sky_sframe.summary_entropy_night("daily", 20220500+i, sample_lambda=True)
        #desientropy.raw_exp.summary_entropy_night(20220500 + i)
