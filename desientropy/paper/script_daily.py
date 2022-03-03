import desientropy.redrock as redrock_entropy


redrock_entropy.summary_release_entropy("daily")
#redrock_entropy.summary_release_entropy("daily", lastnight=20220301)

#for i in range(1,29):
#	redrock_entropy.summary_release_entropy("daily", lastnight=20220200+i)