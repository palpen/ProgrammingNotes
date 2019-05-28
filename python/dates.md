# Notes on dates and other time objects in Python

## Common date formats
[Date format codes](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

Day
```
%d | Day of the month zero-padded decimal number | 01, 02, …, 31
```

Month
```
%b | Month as locale’s abbreviated name | Jan, Feb, …, Dec (en_US);
%m | Month as a zero-padded decimal number | 01, 02, …, 12
```

Year
```
%y | Year without century as a zero-padded decimal number | 00, 01, …, 99
%Y | Year with century as a decimal number | 1970, 1988, 2001, 2013
```

Hour, minute, seconds
```
%H | Hour (24-hour clock) as a zero-padded decimal number | 00, 01, …, 23
%I | Hour (12-hour clock) as a zero-padded decimal number | 01, 02, …, 12
%p | Locale’s equivalent of either AM or PM | AM, PM (en_US);
%M | Minute as a zero-padded decimal number | 00, 01, …, 59
%S | Second as a zero-padded decimal number | 00, 01, …, 59
```
