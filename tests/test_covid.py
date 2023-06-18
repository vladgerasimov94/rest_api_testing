from assertpy import assert_that

from clients.covid_tracker.covid_tracker_client import covid_tracker_client
from helpers.covid_tracker_helper import CovidTrackerHelper


def test_covid_cases_have_crossed_a_million():
    response_xml = covid_tracker_client.get_latest_summary_info()
    total_cases = CovidTrackerHelper.search_nodes_using_xpath(
        response_xml, xpath_expression="//data/summary/total_cases"
    )
    assert_that(int(total_cases)).is_greater_than(1000000)


def test_overall_covid_cases_match_sum_of_total_cases_by_country():
    response_xml = covid_tracker_client.get_latest_summary_info()

    overall_cases = int(
        CovidTrackerHelper.search_nodes_using_xpath(response_xml, xpath_expression="//data/summary/total_cases")
    )
    cases_by_country = CovidTrackerHelper.get_covid_cases_by_country(response_xml=response_xml)

    assert_that(overall_cases).is_greater_than(cases_by_country)
