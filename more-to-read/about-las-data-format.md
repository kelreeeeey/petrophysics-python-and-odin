# LAS Data format

## CWLS Log ASCII Standard-VERSION 2.0

One might google/bing/ask AI for what is "LAS" actually means, here'se some i found:

1. LAS is shorthand for _LASer_ that design for the interchange and archiving [**lidar point clouds**](https://www.asprs.org/wp-content/uploads/2010/12/LAS_Specification.pdf)
2. LAS is an abreviation of "Log ASCII Standard" design storing and distributing digital [**well log data**](https://www.usgs.gov/programs/national-geological-and-geophysical-data-preservation-program/well-log-data)

This repo's interest is the second one, LAS as it for well log data.
LAS format in that case, was design by CWSL.

CWLS stands for [ _Canadian Well Logging Society_ ](https://www.cwls.org/)

>[!INFO]- What is CWLS
> The CWLS (Canadian Well Logging Society) is the oldest organization devoted to log analysis, incorporated in Calgary, Canada in 1957. In that time the society has endeavoured to produce a technical journal with a Canadian slant. The CWLS is thus an appropriate place for those interested in exploring mineral resources in the Western Canadian Sedimentary Basin, the Canadian Arctic, offshore eastern Canada and southern Ontario.

That format is broadly being used in common oil and gass (OnG) industry.

There are several Python package that are being developed in concern of working
with LAS file format. I suggest you to use

1. [lasio](https://github.com/kinverarity1/lasio), or
2. [welly](https://github.com/agilescientific/welly).
