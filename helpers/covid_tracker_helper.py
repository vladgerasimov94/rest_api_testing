from jsonpath_ng import parse
from lxml import etree


class CovidTrackerHelper:
    @staticmethod
    def search_nodes_using_xpath(response_xml, xpath_expression):
        xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
        return xml_tree.xpath(xpath_expression)[0].text

    @staticmethod
    def get_covid_cases_by_country(response_xml, xpath_expression="//data//regions//total_cases"):
        xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
        search_for = etree.XPath(xpath_expression)
        cases_by_country = 0
        for region in search_for(xml_tree):
            cases_by_country += int(region.text)
        return cases_by_country
