# -*- coding: utf-8 -*-
"""
Вывести на экран все двузначные числа, сумма цифр которых делится на 7 \

"""

print [x for x in range(10, 100) if (x % 10 + x / 10) % 7 == 0]
# very cute now. thx @BumagniyPacket
