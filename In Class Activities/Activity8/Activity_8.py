# Jacob Williamson
# CYBR493A
# Fall24
# Activity #8
# November 1, 2024

import Web_Scraping_xml as wb

def main():
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Grabbing the header of the page and removing white space and extra characters
    header = main_tree.xpath('normalize-space(/html/body/header/div/a/text())')
    print(header)
    # Getting the heading from the page and removing white space and extra characters
    heading = main_tree.xpath('normalize-space(//*[@id="wvu-main"]/div[3]/div/div[1]/h2/text())')
    print(heading)
    # Finding upcoming event names from the calendar
    eventNames = main_tree.xpath('//div[@class="wvu-calendar-widget__feed"]//span[@class="eventName"]/a/text()')
    print(eventNames)
    # Grabbing all the quick links
    quickLinks = main_tree.xpath('//*[@id="wvu-main"]/div[4]/div/div[2]/ul/li/a/text()')
    print(quickLinks)
    # Found the featurettes underneath the Let Us Be Your Guide section
    featurettes = main_tree.xpath('//*[@id="resources"]//h3/text()')
    print(featurettes)

if __name__ == "__main__":
    main()
