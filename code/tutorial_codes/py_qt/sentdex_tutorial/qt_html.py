import os
import sys
from PyQt4.QtCore import QUrl, SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebPage, QWebView
from urllib2 import urlopen

JQUERY_URL = 'https://code.jquery.com/jquery-3.3.1.min.js'
JQUERY_FILE = JQUERY_URL.split('/')[-1]
JQUERY_PATH = os.path.join(os.path.dirname(__file__), JQUERY_FILE)


def get_jquery(jquey_url=JQUERY_URL, jquery_path = JQUERY_PATH):

    """
        Returns jquery source.

        If the source is not available at jquery_path, then we will download it from
        jquery_url.
    """
    if not os.path.exists(jquery_path):
        jquery = urlopen(jquey_url).read()
        f = open(jquery_path, 'w')
        f.write(jquery)
        f.close()
    else:
        f = open(jquery_path)
        jquery = f.read()
        f.close()
    return jquery


class WebPage(QWebPage):
    """
       QWebPage that prints Javascript errors to stderr.
    """

    def javaScriptConsoleMessage(self, message, lineNumber, sourceID):
           sys.stderr.write('Javascript error at line number %d\n' % lineNumber)
           sys.stderr.write('%s\n' % message)
           sys.stderr.write('Source ID: %s\n' % sourceID)

class GoogleSearchBot(QApplication):

    def __init__(self, argv, show_window=True):
        super(GoogleSearchBot, self).__init__(argv)
        self.jquery = get_jquery()
        self.web_view = QWebView()
        self.web_page = WebPage()
        self.web_view.setPage(self.web_page)

        if show_window is True:
            self.web_view.show()
        self.connect(self.web_view, SIGNAL("loadFinished(bool)"), self.load_finished)
        self.set_load_function(None)

    def google_search(self, keyword_string):
        self.set_load_function(self.parse_google_search)
        current_frame = self.web_view.page().currentFrame()
        current_frame.evaluateJavaScript(
            r"""
            $("input[title=Google Search]").val("%s");
            $("input[value=Google Search]").parents("form").submit();
            """ % keyword_string
        )

    def load_finished(self, ok):
        current_frame = self.web_page.currentFrame()
        current_frame.evaluateJavaScript(self.jquery)
        self.load_function(*self.load_function_args,
            **self.load_function_kwargs)

    def parse_google_search(self):
        current_frame = self.web_page.currentFrame()
        results = current_frame.evaluateJavaScript(
            r"""
                        var results = "";
                        $("h3[class=r]").each(function(i) {
                            results += $(this).text() + "\n";
                        });
                        results;
                        """
        )
        print('Google search result\n====================')
        for i, result in enumerate(unicode(results.toString(), 'utf-8').splitlines()):
            print('%d. %s' % (i + 1, result))
        self.exit()

    def search(self, keyword):
        self.set_load_function(self.google_search, keyword)
        self.web_page.currentFrame().load(QUrl('http://www.google.com/'))

    def set_load_function(self, load_function,*args, **kwargs):
        self.load_function = load_function
        self.load_function_args = args
        self.load_function_kwargs = kwargs

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage: %s <keyword>" % sys.argv[0])
        raise SystemExit, 255

    googleSearchBot = GoogleSearchBot(sys.argv)
    googleSearchBot.search(sys.argv[1])
    sys.exit(googleSearchBot.exec_())
