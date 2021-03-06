class Views(object):

    MARKERS_HEBREW_VIEW = """SELECT markers.id,
                                    markers.provider_and_id,
                                    markers.provider_code,
                                    provider_code.provider_code_hebrew,
                                    markers.accident_type,
                                    accident_type.accident_type_hebrew,
                                    markers.accident_severity,
                                    accident_severity.accident_severity_hebrew,
                                    markers.location_accuracy,
                                    location_accuracy.location_accuracy_hebrew,
                                    markers.road_type,
                                    road_type.road_type_hebrew,
                                    markers.road_shape,
                                    road_shape.road_shape_hebrew,
                                    markers.day_type,
                                    day_type.day_type_hebrew,
                                    markers.police_unit,
                                    police_unit.police_unit_hebrew,
                                    markers.one_lane,
                                    one_lane.one_lane_hebrew,
                                    markers.multi_lane,
                                    multi_lane.multi_lane_hebrew,
                                    markers.speed_limit,
                                    speed_limit.speed_limit_hebrew,
                                    markers.road_intactness,
                                    road_intactness.road_intactness_hebrew,
                                    markers.road_width,
                                    road_width.road_width_hebrew,
                                    markers.road_sign,
                                    road_sign.road_sign_hebrew,
                                    markers.road_light,
                                    road_light.road_light_hebrew,
                                    markers.road_control,
                                    road_control.road_control_hebrew,
                                    markers.weather,
                                    weather.weather_hebrew,
                                    markers.road_surface,
                                    road_surface.road_surface_hebrew,
                                    markers.road_object,
                                    road_object.road_object_hebrew,
                                    markers.object_distance,
                                    object_distance.object_distance_hebrew,
                                    markers.didnt_cross,
                                    didnt_cross.didnt_cross_hebrew,
                                    markers.cross_mode,
                                    cross_mode.cross_mode_hebrew,
                                    markers.cross_location,
                                    cross_location.cross_location_hebrew,
                                    markers.cross_direction,
                                    cross_direction.cross_direction_hebrew,
                                    markers.road1,
                                    markers.road2,
                                    markers.km,
                                    markers.yishuv_symbol,
                                    markers.yishuv_name,
                                    markers.geo_area,
                                    geo_area.geo_area_hebrew,
                                    markers.day_night,
                                    day_night.day_night_hebrew,
                                    markers.day_in_week,
                                    day_in_week.day_in_week_hebrew,
                                    markers.traffic_light,
                                    traffic_light.traffic_light_hebrew,
                                    markers.region,
                                    region.region_hebrew,
                                    markers.district,
                                    district.district_hebrew,
                                    markers.natural_area,
                                    natural_area.natural_area_hebrew,
                                    markers.municipal_status,
                                    municipal_status.municipal_status_hebrew,
                                    markers.yishuv_shape,
                                    yishuv_shape.yishuv_shape_hebrew,
                                    markers.street1,
                                    markers.street1_hebrew,
                                    markers.street2,
                                    markers.street2_hebrew,
                                    markers.non_urban_intersection_hebrew,
                                    markers.accident_year,
                                    markers.accident_month,
                                    markers.accident_day,
                                    markers.accident_hour_raw,
                                    accident_hour_raw.accident_hour_raw_hebrew,
                                    markers.accident_hour,
                                    markers.accident_minute,
                                    markers.geom,
                                    markers.longitude,
                                    markers.latitude,
                                    markers.x,
                                    markers.y
                                   FROM markers
                                     LEFT JOIN accident_type ON markers.accident_type = accident_type.id AND markers.accident_year = accident_type.year AND markers.provider_code = accident_type.provider_code
                                     LEFT JOIN accident_severity ON markers.accident_severity = accident_severity.id AND markers.accident_year = accident_severity.year AND markers.provider_code = accident_severity.provider_code
                                     LEFT JOIN location_accuracy ON markers.location_accuracy = location_accuracy.id AND markers.accident_year = location_accuracy.year AND markers.provider_code = location_accuracy.provider_code
                                     LEFT JOIN road_type ON markers.road_type = road_type.id AND markers.accident_year = road_type.year AND markers.provider_code = road_type.provider_code
                                     LEFT JOIN road_shape ON markers.road_shape = road_shape.id AND markers.accident_year = road_shape.year AND markers.provider_code = road_shape.provider_code
                                     LEFT JOIN day_type ON markers.day_type = day_type.id AND markers.accident_year = day_type.year AND markers.provider_code = day_type.provider_code
                                     LEFT JOIN police_unit ON markers.police_unit = police_unit.id AND markers.accident_year = police_unit.year AND markers.provider_code = police_unit.provider_code
                                     LEFT JOIN one_lane ON markers.one_lane = one_lane.id  AND markers.accident_year = one_lane.year AND markers.provider_code = one_lane.provider_code
                                     LEFT JOIN multi_lane ON markers.multi_lane = multi_lane.id AND markers.accident_year = multi_lane.year AND markers.provider_code = multi_lane.provider_code
                                     LEFT JOIN speed_limit ON markers.speed_limit = speed_limit.id AND markers.accident_year = speed_limit.year AND markers.provider_code = speed_limit.provider_code
                                     LEFT JOIN road_intactness ON markers.road_intactness = road_intactness.id AND markers.accident_year = road_intactness.year AND markers.provider_code = road_intactness.provider_code
                                     LEFT JOIN road_width ON markers.road_width = road_width.id AND markers.accident_year = road_width.year AND markers.provider_code = road_width.provider_code
                                     LEFT JOIN road_sign ON markers.road_sign = road_sign.id AND markers.accident_year = road_sign.year AND markers.provider_code = road_sign.provider_code
                                     LEFT JOIN road_light ON markers.road_light = road_light.id AND markers.accident_year = road_light.year AND markers.provider_code = road_light.provider_code
                                     LEFT JOIN road_control ON markers.road_control = road_control.id AND markers.accident_year = road_control.year AND markers.provider_code = road_control.provider_code
                                     LEFT JOIN weather ON markers.weather = weather.id AND markers.accident_year = weather.year AND markers.provider_code = weather.provider_code
                                     LEFT JOIN road_surface ON markers.road_surface = road_surface.id AND markers.accident_year = road_surface.year AND markers.provider_code = road_surface.provider_code
                                     LEFT JOIN road_object ON markers.road_object = road_object.id AND markers.accident_year = road_object.year AND markers.provider_code = road_object.provider_code
                                     LEFT JOIN object_distance ON markers.object_distance = object_distance.id AND markers.accident_year = object_distance.year AND markers.provider_code = object_distance.provider_code
                                     LEFT JOIN didnt_cross ON markers.didnt_cross = didnt_cross.id AND markers.accident_year = didnt_cross.year AND markers.provider_code = didnt_cross.provider_code
                                     LEFT JOIN cross_mode ON markers.cross_mode = cross_mode.id AND markers.accident_year = cross_mode.year AND markers.provider_code = cross_mode.provider_code
                                     LEFT JOIN cross_location ON markers.cross_location = cross_location.id AND markers.accident_year = cross_location.year AND markers.provider_code = cross_location.provider_code
                                     LEFT JOIN cross_direction ON markers.cross_direction = cross_direction.id AND markers.accident_year = cross_direction.year AND markers.provider_code = cross_direction.provider_code
                                     LEFT JOIN geo_area ON markers.geo_area = geo_area.id AND markers.accident_year = geo_area.year AND markers.provider_code = geo_area.provider_code
                                     LEFT JOIN day_night ON markers.day_night = day_night.id AND markers.accident_year = day_night.year AND markers.provider_code = day_night.provider_code
                                     LEFT JOIN day_in_week ON markers.day_in_week = day_in_week.id AND markers.accident_year = day_in_week.year AND markers.provider_code = day_in_week.provider_code
                                     LEFT JOIN traffic_light ON markers.traffic_light = traffic_light.id AND markers.accident_year = traffic_light.year AND markers.provider_code = traffic_light.provider_code
                                     LEFT JOIN region ON markers.region = region.id AND markers.accident_year = region.year AND markers.provider_code = region.provider_code
                                     LEFT JOIN district ON markers.district = district.id AND markers.accident_year = district.year AND markers.provider_code = district.provider_code
                                     LEFT JOIN natural_area ON markers.natural_area = natural_area.id AND markers.accident_year = natural_area.year AND markers.provider_code = natural_area.provider_code
                                     LEFT JOIN municipal_status ON markers.municipal_status = municipal_status.id AND markers.accident_year = municipal_status.year AND markers.provider_code = municipal_status.provider_code
                                     LEFT JOIN yishuv_shape ON markers.yishuv_shape = yishuv_shape.id AND markers.accident_year = yishuv_shape.year AND markers.provider_code = yishuv_shape.provider_code
                                     LEFT JOIN accident_hour_raw ON markers.accident_hour_raw = accident_hour_raw.id AND markers.accident_year = accident_hour_raw.year AND markers.provider_code = accident_hour_raw.provider_code
                                     LEFT JOIN provider_code ON markers.provider_code = provider_code.id;"""

    INVOLVED_HEBREW_VIEW = """SELECT involved.accident_id,
    involved.provider_and_id,
    involved.provider_code,
    involved.involved_type,
    involved_type.involved_type_hebrew,
    involved.license_acquiring_date,
    involved.age_group,
    age_group.age_group_hebrew,
    involved.sex,
    sex.sex_hebrew,
    involved.vehicle_type,
    vehicle_type.vehicle_type_hebrew,
    involved.safety_measures,
    safety_measures.safety_measures_hebrew,
    involved.involve_yishuv_symbol,
    involved.involve_yishuv_name,
    involved.injury_severity,
    injury_severity.injury_severity_hebrew,
    involved.injured_type,
    injured_type.injured_type_hebrew,
    involved.injured_position,
    injured_position.injured_position_hebrew,
    involved.population_type,
    population_type.population_type_hebrew,
    involved.home_region,
    region.region_hebrew,
    involved.home_district,
    district.district_hebrew AS home_district_hebrew,
    involved.home_natural_area,
    natural_area.natural_area_hebrew AS home_natural_area_hebrew,
    involved.home_municipal_status,
    municipal_status.municipal_status_hebrew,
    involved.home_residence_type,
    yishuv_shape.yishuv_shape_hebrew AS home_residence_type_hebrew,
    involved.hospital_time,
    hospital_time.hospital_time_hebrew,
    involved.medical_type,
    medical_type.medical_type_hebrew,
    involved.release_dest,
    release_dest.release_dest_hebrew,
    involved.safety_measures_use,
    safety_measures_use.safety_measures_use_hebrew,
    involved.late_deceased,
    late_deceased.late_deceased_hebrew,
    involved.car_id,
    involved.involve_id,
    involved.accident_year,
    involved.accident_month
   FROM involved
     LEFT JOIN involved_type ON involved.involved_type = involved_type.id AND involved.accident_year = involved_type.year AND involved.provider_code = involved_type.provider_code
     LEFT JOIN age_group ON involved.age_group = age_group.id  AND involved.accident_year = age_group.year AND involved.provider_code = age_group.provider_code
     LEFT JOIN sex ON involved.sex = sex.id AND involved.accident_year = sex.year AND involved.provider_code = sex.provider_code
     LEFT JOIN vehicle_type ON involved.vehicle_type = vehicle_type.id AND involved.accident_year = vehicle_type.year AND involved.provider_code = vehicle_type.provider_code
     LEFT JOIN safety_measures ON involved.safety_measures = safety_measures.id AND involved.accident_year = safety_measures.year AND involved.provider_code = safety_measures.provider_code
     LEFT JOIN injury_severity ON involved.injury_severity = injury_severity.id AND involved.accident_year = injury_severity.year AND involved.provider_code = injury_severity.provider_code
     LEFT JOIN injured_type ON involved.injured_type = injured_type.id AND involved.accident_year = injured_type.year AND involved.provider_code = injured_type.provider_code
     LEFT JOIN injured_position ON involved.injured_position = injured_position.id AND involved.accident_year = injured_position.year AND involved.provider_code = injured_position.provider_code
     LEFT JOIN population_type ON involved.population_type = population_type.id AND involved.accident_year = population_type.year AND involved.provider_code = population_type.provider_code
     LEFT JOIN region ON involved.home_region = region.id AND involved.accident_year = region.year AND involved.provider_code = region.provider_code
     LEFT JOIN district ON involved.home_district = district.id AND involved.accident_year = district.year AND involved.provider_code = district.provider_code
     LEFT JOIN natural_area ON involved.home_natural_area = natural_area.id AND involved.accident_year = natural_area.year AND involved.provider_code = natural_area.provider_code
     LEFT JOIN municipal_status ON involved.home_municipal_status = municipal_status.id AND involved.accident_year = municipal_status.year AND involved.provider_code = municipal_status.provider_code
     LEFT JOIN yishuv_shape ON involved.home_residence_type = yishuv_shape.id AND involved.accident_year = yishuv_shape.year AND involved.provider_code = yishuv_shape.provider_code
     LEFT JOIN hospital_time ON involved.hospital_time = hospital_time.id AND involved.accident_year = hospital_time.year AND involved.provider_code = hospital_time.provider_code
     LEFT JOIN medical_type ON involved.medical_type = medical_type.id AND involved.accident_year = medical_type.year AND involved.provider_code = medical_type.provider_code
     LEFT JOIN release_dest ON involved.release_dest = release_dest.id AND involved.accident_year = release_dest.year AND involved.provider_code = release_dest.provider_code
     LEFT JOIN safety_measures_use ON involved.safety_measures_use = safety_measures_use.id AND involved.accident_year = safety_measures_use.year AND involved.provider_code = safety_measures_use.provider_code
     LEFT JOIN late_deceased ON involved.late_deceased = late_deceased.id AND involved.accident_year = late_deceased.year AND involved.provider_code = late_deceased.provider_code;"""

    VEHICLES_HEBREW_VIEW = """ SELECT vehicles.id,
    vehicles.accident_id,
    vehicles.provider_and_id,
    vehicles.provider_code,
    vehicles.engine_volume,
    engine_volume.engine_volume_hebrew,
    vehicles.manufacturing_year,
    vehicles.driving_directions,
    driving_directions.driving_directions_hebrew,
    vehicles.vehicle_status,
    vehicle_status.vehicle_status_hebrew,
    vehicles.vehicle_attribution,
    vehicle_attribution.vehicle_attribution_hebrew,
    vehicles.seats,
    vehicles.total_weight,
    total_weight.total_weight_hebrew,
    vehicles.vehicle_type,
    vehicle_type.vehicle_type_hebrew
   FROM vehicles
     LEFT JOIN engine_volume ON vehicles.engine_volume = engine_volume.id AND vehicles.accident_year = engine_volume.year AND vehicles.provider_code = engine_volume.provider_code
     LEFT JOIN driving_directions ON vehicles.driving_directions = driving_directions.id AND vehicles.accident_year = driving_directions.year AND vehicles.provider_code = driving_directions.provider_code
     LEFT JOIN vehicle_status ON vehicles.vehicle_status = vehicle_status.id AND vehicles.accident_year = vehicle_status.year AND vehicles.provider_code = vehicle_status.provider_code
     LEFT JOIN vehicle_attribution ON vehicles.vehicle_attribution = vehicle_attribution.id AND vehicles.accident_year = vehicle_attribution.year AND vehicles.provider_code = vehicle_attribution.provider_code
     LEFT JOIN vehicle_attribution ON vehicles.vehicle_attribution = vehicle_attribution.id AND vehicles.accident_year = vehicle_attribution.year AND vehicles.provider_code = vehicle_attribution.provider_code
     LEFT JOIN vehicle_type ON vehicles.vehicle_type = vehicle_type.id AND vehicles.accident_year = vehicle_type.year AND vehicles.provider_code = vehicle_type.provider_code;"""

VIEWS = Views()
