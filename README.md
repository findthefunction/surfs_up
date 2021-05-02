# Surfs Up

## Analysis

The purpose of this assignment is to determine the optimal location for a surf and icecream shop using temperature data and leveraging the power of Python, SQLAlchemy, SQLite and Flask.

## Overview of the statistical analysis:

In order to compile and analyse the temperature data we created an sqlite engine and reflected the tables containing measurement and station data into a new model.

We then created a query to retrieve the temperatures from the measurement table and extract all the june data.  The same steps were repeated for the December data. 

![dec_summary](https://user-images.githubusercontent.com/31022640/116828165-d473ed80-ab51-11eb-8d9e-7b7a501e93c7.png)
![june_summary](https://user-images.githubusercontent.com/31022640/116828166-d50c8400-ab51-11eb-869b-a1422b93c8dc.png)

## Results

The key three differences between the statistical analysis performed on Decemeber and June:

- June had a larger number of temperature readings in relation to December.
- The minimum temperature was 8 degrees lower in December (56 degrees) than Junes temperature of 64 degrees.
- The mean temperatures were within 3 degrees of each other which is favourable.

## Summary

In summation the target location for the ice cream surf shop is favourable based on the limited temperature variances being as they are generally always in a favourable range.  Additional information that could be included in this analysis would be to perform precipitation queries and to analyses other weather factors such as day length and wind speeds.

