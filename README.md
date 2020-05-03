# airbnb_analysis
airbnb_analysis
### Libraries Used:-
- **pandas**
- **numpy**
- **sklearn**
- **matplotlib**
- **seaborn**
- **folium**

### Goal from project:-
- 1)identify what affects the price of listing
- 2)Build a model that can predict the price of listing

**Answer these qustions**
- What features have the highest correlation with the price?
- Can we predict the price from the given features?
- Can we predict the weekly and monthly price from the price?
- Is there a price difference between Boston and Seattle?
- Do local postings from hosts in the same city value higher then remote postings?

### Data Sources:-
**Two avoid bias I merged two datasets from two different cities to get a clear picure of what influences a price in general. The two datasets are:-**
- **Seattle AirBNB Data : https://www.kaggle.com/airbnb/seattle/data.**
- **Boston AirBNB Data : https://www.kaggle.com/airbnb/boston**
- **ZipCode Data: https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/export/**

Medium link:https://medium.com/@isbader95/airbnb-boston-seattle-analysis-df053abb93f7?sk=1f3fa5c14ff300faba75cdbec331d426

### Data prepration summary 

|Feature|Old_type|Action|New_type|
|---|---|---|---|
|**listing_url**|`object`|Delete since the URL is not needed||
|**picture_url**|`object`|Delete since the URL is not needed||
|**xl_picture_url**|`object`|Delete since the URL is not needed||
|**host_url**|`object`|Delete since the URL is not needed||
|**host_thumbnail_url**|`object`|Delete since the URL is not needed||
|**medium_url**|`object`|Delete since the URL is not needed||
|**thumbnail_url**|`object`|Delete since the URL is not needed||
|**host_picture_url**|`object`|Delete since the URL is not needed||
|---|---|---|---|
|**square_feet**|`float64`|Delete since %97 of data is missing||
|**license**|`float64`|Delete since %100 of data is missing||
|**country**|`object`|Delete to avoid redundency|
|**experiences_offered**|`object`|delete since all values are none|
|---|---|---|---|
|**price**|`object`|Remove dollar sign and punctuations|`Float64`|
|**weekly_price**|`object`|Remove dollar sign and punctuations then try to predict|`Float64`|
|**monthly_price**|`object`|Remove dollar sign and punctuations then try to predict|`Float64`|
|**security_deposit**|`object`|replace null values with 0|`Float64`|
|**cleaning_fee**|`object`|replace null values with 0|`Float64`|
|**guests_included**|`int64`|clean|`int64`
|**extra_people**|`object`|Remove dollar sign and punctuations|`Float64`|
|---|---|---|---|
|**summary**|`object`|Get the word count insted|`int64`|
|**space**|`object`|Get the word count insted|`int64`|
|**description**|`object`|Get the word count insted|`int64`|
|**neighborhood_overview**|`object`|Get the word count insted|`int64`|
|**transit**|`object`|Get the word count insted|`int64`|
|**host_about**|`object`|Get the word count insted|`int64`|
|**notes**|`object`|Get the word count insted|`int64`|
|---|---|---|---|
|**host_location**|`object`|Fill missing values with 'unknown' and grab only the city|`object`|
|**smart_location**|`object`|split to grab the city only and change to lower case|`object`|
|**state**|`object`|Change all to lower case|`object`|
|**latitude**|`Float`|clean|`Float`|
|**longitude**|`Float`|clean|`Float`|
|**neighbourhood**|`object`|fill missing values from neighbourhood_cleansed|`object`|
|**is_location_exact**|`object`|change to bool|`int64`|
|**zipcode**|`object`|clean to get the digits only|`int64`|
|**host_match**|`int64`|added bool feature to check post and host location match|`int64`|
|**street**|`object`|delete I will not be using it|
|**country_code**|`object`|delete I will not be using it|
|**city**|`object`|delete to avoid redundency|
|**neighbourhood_group_cleansed**|`object`|delete to avoid redundency|
|**neighbourhood_cleansed**|`object`|delete to avoid redundency|
|---|---|---|---|
|**host_id**|`int64`|clean|`int64`|
|**host_name**|`object`|replace null with none|`object`|
|**host_since**|`date_time`|replace null with median|`datetime64`|
|**host_response_time**|`object`|replace null with none|`object`|
|**host_response_rate**|`object`|replace from median|`float64`|
|**host_acceptance_rate**|`object`|replace from median|`float64`|
|**host_is_superhost**|`object`|replace with int bool|`int64`|
|**host_neighbourhood**|`object`|delete unnecessary|
|**host_year**|`int64`|created this new column to represent the year the host joined|`int64`|
|---|---|---|---|
|**host_listings_count**|`float64`|replace null with mean|`int64`|
|**host_total_listings_count**|`float64`|Delete to avoid redundency|
|**host_has_profile_pic**|`object`|change to bool and replace null with 0|`int64`|
|**host_identity_verified**|`object`|change to bool and replace null with 0|`int64`|
|**host_verifications**|`object`|Replace with the number of verifications|`int64`|
|**market**|`object`|delete to avoid redundency|
|---|---|---|---|
|**property_type**|`object`|replace null with mode|`object`|
|**room_type**|`object`|replace null with mode|`object`|
|**accommodates**|`int64`|clean|`int64`|
|**bathrooms**|`float64`|replace null values with mode|`float64`|
|**bedrooms**|`float64`|replace null values with mode|`float64`|
|**beds**|`float64`|replace missing with the mode|`float64`|
|**bed_type**|`object`|clean|`object`|
|**amenities**|`object`|get the count of amenities|`int64`|
|---|---|---|---|
|**number_of_reviews**|`int64`|clean|`int64`|
|**first_review**|`object`|change to date-time fromat and clean|`datetime64`|
|**last_review**|`object`|change to date-time format and clean|`datetime64`|
|**review_scores_rating**|`float64`|replace null values with mean|`float64`|
|**review_scores_accuracy**|`float64`|replace null values with mean|`float64`|
|**review_scores_cleanliness**|`float64`|replace null values with mean|`float64`|
|**review_scores_checkin**|`float64`|replace null values with mean|`float64`|
|**review_scores_communication**|`float64`|replace null values with mean|`float64`|
|**review_scores_location**|`float64`|replace null values with mean|`float64`|
|**review_scores_value**|`float64`|replace null values with mean|`float64`|
|---|---|---|---|
|**minimum_nights**|`int64`|clean|`int64`|
|**maximum_nights**|`int64`|clean|`int64`|
|**calendar_updated**|`object`|clean|`object`|
|**has_availability**|`object`|change with int bool and fill null with 0|`int64`|
|**availability_30**|`int64`|clean|`int64`|
|**availability_60**|`int64`|clean|`int64`|
|**availability_90**|`int64`|clean|`int64`|
|**availability_365**|`int64`|clean|`int64`|
|**calendar_last_scraped**|`object`|unnecessary delete|
|---|---|---|---|
|**instant_bookable**|`object`|change to int bool|`int64`|
|**cancellation_policy**|`object`|clean|`object`|
|**instant_bookable**|`object`|change to int bool|`int64`|
|**require_guest_profile_picture**|`float64`|change to int bool|`int64`|
|**require_guest_phone_verification**|`float64`|change to int bool|`int64`|
|**calculated_host_listings_count**|`int64`|clean|`int64`|
|**reviews_per_month**|`float64`|fill missing with mean|`float64`|
|**requires_license**|`object`|change to int bool (delete since all values are false)|
|**jurisdiction_names**|`object`|delete not nacassery|


