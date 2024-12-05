import Web_Scraping as wb


"""
This will be our main screen
"""


def main():
    # Your code goes here.
    main_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&"
    links = generate_links(main_link)
    while True:
        user_input = input(f'Which page would you like to view? (0 to {len(links) - 1}), or type "exit" to quit):')
        if user_input == 'exit':
            break
        try:
            # need to convert user input to int if input != exit
            pageNum = int(user_input)
            if 0 <= pageNum <= len(links):
                display_bugs_info(links[pageNum])
            else:
                print("Invalid input. Please choose a valid page number.")
        except ValueError:
            print("Please enter a valid number.")

def generate_links(start_link):
    """
        This method generates ALL the links to all pages and stores them in a list (This is activity #10)
        :param start_link: The start link of the bug tracking system.
        :return: The list of all pages to all bugs. Each element in the list will refer to one page
    """
    list_of_links = []
    pageCount = 0
    bugsPerPage = 75

    while True:
        new_start = pageCount * bugsPerPage
        new_page = f"{start_link}&start={new_start}"

        web_tree = wb.get_web_tree(new_page)
        bugRows = web_tree.xpath('//*[@class="buglisting-row"]')
        if pageCount >= 5:  # Process only the first 10 pages for now
            break
        if not bugRows:
            break
        # everytime you get a link to a new page, use list_of_links.append(new_page)
        list_of_links.append(new_page)
        print(f"Fetching page {pageCount + 1}, URL: {new_page}")
        pageCount += 1

    print(f"Generated {len(list_of_links)} links.")

    return list_of_links

def display_bugs_info(bugs_page):
    """
        This method displays the bugs info. for a specific page
        Display: Bug Number, Title, Importance, and Heat - in this order for each bug.(This is activities #11 and 12)
        :param bugs_page: The  link to the page
    """
    web_tree = wb.get_web_tree(bugs_page)
    bug_rows = web_tree.xpath('//*[@class="buglisting-row"]')

    print(f"Displaying bugs for: {bugs_page}\n")
    for bug in bug_rows:
        bugImportance = bug.xpath('.//div["buglisting-col1"]//text()')
        number = bugImportance[9].strip()
        severity = bugImportance[1].strip()
        status = bugImportance[3].strip()
        heat = bugImportance[18].strip()
        summary = bugImportance[11].strip()

        print(f"{number}, {severity}, {status}, {heat}, {summary}")

if __name__ == "__main__":
    main()
