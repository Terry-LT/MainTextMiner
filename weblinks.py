from googlesearch import search
import trafilatura
from messages import print_out_of_range,print_must_be_int
from validate import *
from userinput import *
from ai import summarize_info
from saveinfo import create_file,copy_to_clipboard

class WebLinks:
    url = ""
    info_to_search = ""
    range_results = 0
    links_results = []
    text = ""

    def get_web_links(self):
        results = search(term=self.info_to_search, num_results=self.range_results, lang="eu")
        results = list(results)

        index = 0
        print("Now choose by number:")
        for link in results:
            print(index,link)
            index += 1
        self.links_results = results
        return results

    def set_url(self,number_of_link):

        if validate_int(number_of_link):
            if (0 <= int(number_of_link)) and (int(number_of_link) <= self.links_results.__len__()):
                # Save num of results
                self.url = self.links_results[int(number_of_link)]
            else:
                print_out_of_range()
        else:
            print_must_be_int()

    def save_text(self):
        if not validate_last_element_of_url(self.url):
            self.url = self.url[:-1]

        text = trafilatura.fetch_url(self.url)
        text = trafilatura.extract(text)

        # TODO check from confing file, if user want to use AI to summarize text
        text = summarize_info(text)

        choose = input("Do you want to copy text to clipboard or save as a file? Type +(text to clipboard) -(save as a file)")
        if remove_all_spaces(choose) == "+":
            copy_to_clipboard(text)
        else:
            create_file(text)

    def youtube_video(self,range_results):
        pass
    def user_input_text(self):
        pass

    def google_command(self,range_results):
        if validate_range_response(range_results):
            # Save range
            self.range_results = int(range_results)
            search_input = input("What do you want to search?:")
            self.info_to_search = search_input
            links = self.get_web_links()
            number_of_order = input("Choose number:")
            if validate_int(number_of_order):
                self.set_url(number_of_order)
                self.save_text()
            else:
                print_must_be_int()

    def paste_link_command(self,url):
        if validate_url(url):
            self.url = url
            self.save_text()