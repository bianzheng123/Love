class Boy():
    def __init__(self, name):
        print(name)


class Girl():
    def __init__(self, name):
        print(name)


"""
This is the code in python.
Also, this is the gift to celebrate our 1st anniversary.
"""
i = Boy('Bian')
u = Girl('Astraeaw')
# May 14, 2020, I told you I love you.
i.love(u)
# Luckily, you accepted and became my girlfriend.
u.accepted()
# Since then, I miss you every day
i.miss(u)
# I always take care of you
i.takeCareOf(u)
# You said that you would marry me as long as I am 23.
# I can't wait to become 23 and marry you.
is23 = False
while i.is23():
    i.getOlder()
    # As time goes by, I will be 23
    # and we would get married at that time
    i.waitFor(u)
# After a romantic wedding, we will live happily since then
i.marry(u)
i.liveHappilyWith(u)