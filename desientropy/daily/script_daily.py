import desientropy.redrock as redrock_entrop
import desientropy.raw_exp
import desientropy.sky_sframe

for i in range(0,10):
	desientropy.redrock.summary_release_entropy("daily", lastnight=20220500+i)
        desientropy.sky_sframe.summary_entropy_night("daily", 20220500+i, sample_lambda=True)
        desientropy.raw_exp.summary_entropy_night(20220500 + i)
