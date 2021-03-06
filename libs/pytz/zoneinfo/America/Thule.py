'''tzinfo timezone information for America/Thule.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Thule(DstTzInfo):
    '''America/Thule timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Thule'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1916,7,28,4,35,8),
d(1991,3,31,6,0,0),
d(1991,9,29,5,0,0),
d(1992,3,29,6,0,0),
d(1992,9,27,5,0,0),
d(1993,4,4,6,0,0),
d(1993,10,31,5,0,0),
d(1994,4,3,6,0,0),
d(1994,10,30,5,0,0),
d(1995,4,2,6,0,0),
d(1995,10,29,5,0,0),
d(1996,4,7,6,0,0),
d(1996,10,27,5,0,0),
d(1997,4,6,6,0,0),
d(1997,10,26,5,0,0),
d(1998,4,5,6,0,0),
d(1998,10,25,5,0,0),
d(1999,4,4,6,0,0),
d(1999,10,31,5,0,0),
d(2000,4,2,6,0,0),
d(2000,10,29,5,0,0),
d(2001,4,1,6,0,0),
d(2001,10,28,5,0,0),
d(2002,4,7,6,0,0),
d(2002,10,27,5,0,0),
d(2003,4,6,6,0,0),
d(2003,10,26,5,0,0),
d(2004,4,4,6,0,0),
d(2004,10,31,5,0,0),
d(2005,4,3,6,0,0),
d(2005,10,30,5,0,0),
d(2006,4,2,6,0,0),
d(2006,10,29,5,0,0),
d(2007,3,11,6,0,0),
d(2007,11,4,5,0,0),
d(2008,3,9,6,0,0),
d(2008,11,2,5,0,0),
d(2009,3,8,6,0,0),
d(2009,11,1,5,0,0),
d(2010,3,14,6,0,0),
d(2010,11,7,5,0,0),
d(2011,3,13,6,0,0),
d(2011,11,6,5,0,0),
d(2012,3,11,6,0,0),
d(2012,11,4,5,0,0),
d(2013,3,10,6,0,0),
d(2013,11,3,5,0,0),
d(2014,3,9,6,0,0),
d(2014,11,2,5,0,0),
d(2015,3,8,6,0,0),
d(2015,11,1,5,0,0),
d(2016,3,13,6,0,0),
d(2016,11,6,5,0,0),
d(2017,3,12,6,0,0),
d(2017,11,5,5,0,0),
d(2018,3,11,6,0,0),
d(2018,11,4,5,0,0),
d(2019,3,10,6,0,0),
d(2019,11,3,5,0,0),
d(2020,3,8,6,0,0),
d(2020,11,1,5,0,0),
d(2021,3,14,6,0,0),
d(2021,11,7,5,0,0),
d(2022,3,13,6,0,0),
d(2022,11,6,5,0,0),
d(2023,3,12,6,0,0),
d(2023,11,5,5,0,0),
d(2024,3,10,6,0,0),
d(2024,11,3,5,0,0),
d(2025,3,9,6,0,0),
d(2025,11,2,5,0,0),
d(2026,3,8,6,0,0),
d(2026,11,1,5,0,0),
d(2027,3,14,6,0,0),
d(2027,11,7,5,0,0),
d(2028,3,12,6,0,0),
d(2028,11,5,5,0,0),
d(2029,3,11,6,0,0),
d(2029,11,4,5,0,0),
d(2030,3,10,6,0,0),
d(2030,11,3,5,0,0),
d(2031,3,9,6,0,0),
d(2031,11,2,5,0,0),
d(2032,3,14,6,0,0),
d(2032,11,7,5,0,0),
d(2033,3,13,6,0,0),
d(2033,11,6,5,0,0),
d(2034,3,12,6,0,0),
d(2034,11,5,5,0,0),
d(2035,3,11,6,0,0),
d(2035,11,4,5,0,0),
d(2036,3,9,6,0,0),
d(2036,11,2,5,0,0),
d(2037,3,8,6,0,0),
d(2037,11,1,5,0,0),
        ]

    _transition_info = [
i(-16500,0,'LMT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
        ]

Thule = Thule()

