from graphene import ObjectType, String, Boolean, ID, Field, Int, Date

class study(ObjectType):
  offical_title = String()
  nct_id = String()
  last_update_submitted_date = Date()
  completion_date = Date()
  study_type = String()
  overall_status = String()
  phase = String()
  why_stopped = String()
  biospec_description = String()
  brief_summary = String()
  detailed_description = String()
  eligibilities_criteria = String()
  min_age = Int()
  max_age = Int()
  gender = String()
  healthy_volunteers = String()
  location_city = String()
  location_name = String()
  url = String()
  keywords = List(String)
  conditions = List(String)
  secondary_outcome_measures = List(String)
  intervention_name = List(String)

class Query(ObjectType):
  study = graphene.Field
