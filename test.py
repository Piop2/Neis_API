import Neis_API

searched_schools = Neis_API.get_school(region_code=Neis_API.R_SEOUL, school_name="서울고등학교")
school = Neis_API.School(searched_schools[0])
