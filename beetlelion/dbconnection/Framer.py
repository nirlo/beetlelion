import aactconnector
import pandas as pd
import psycopg2

engine = aactconnector.getEngine()

query_dict = {
    "studies": "select nct_id,last_update_posted_date,start_date,completion_date,study_type,official_title,overall_status,phase,why_stopped,biospec_description from studies",
    "facilities": "select nct_id, name city from facilities",
    "facility investigators": "select nct_id, name from facility_investigators",
    "countries": "select nct_id, name from countries",
    "keywords": "select nct_id, name from keywords",
    "detailed descriptions": "select nct_id, description from detailed_descriptions",
    "brief summaries": "select nct_id, description from brief_summaries",
    "design groups": "select nct_id, description from design_groups",
    "interventions": "select nct_id, description from interventions",
    "design outcomes": "select nct_id, description from design_outcomes",
    "eligibilities": "select nct_id, description from eligibilities",
    "result groups": "select nct_id, description from result_groups",
    "reported events": "select nct_id, description from reported_events",
    "baseline measurements": "select nct_id, title, description from baseline_measurements",
    "outcome analyses": "select nct_id, method_description, estimate_description, groups_description from outcome_analyses",
    "outcomes": "select nct_id, description from outcomes",
    "outcome measurements": "select nct_id, description, explanation_of_na from outcome_measurements",
    "eligibilities": "select nct_id, minimum_age, maximum_age, population, criteria from eligibilities"
}

def _make_where_clause(nctid):
    return " where nct_id ="+ "'" + nctid + "'"

def _queryDB(sqlstr):
    return pd.read_sql(sqlstr, engine)
    # return pd.read_sql(sqlstr, engine, coerce_float=False, params=None,
    #              parse_dates=None, columns=None, chunksize=None)

def get_DataFrame(nctid):
    return {k:_queryDB(query_dict[k] + _make_where_clause(nctid)) for k in query_dict}
        

