from __future__ import with_statement

from System.Windows.Browser import HtmlPage
from System.Windows.Controls import StackPanel, ComboBoxItem
from System.Windows.Markup import XamlReader



_xaml_cache = {}


class NavigationController(object):
    
    def __init__(self, root, focus_text_box):
        self.root = root
        self.focus_text_box = focus_text_box

    
    
    def change_document(self, part, page):
        fragment = ''
        if part == 0:
            path = 'docs/index.xaml'
        else:
            path = 'docs/part%s/%s' % (part, ('item%s.xaml' % page) if page else 'index.xaml')
            fragment = 'part%s-page%s' % (part, page)
        
        HtmlPage.Window.CurrentBookmark = fragment
        
        if path in _xaml_cache:
            document = _xaml_cache[path]
        else:
            with open(path) as handle:
                xaml = handle.read().decode('utf-8')
            document = XamlReader.Load(xaml)
            _xaml_cache[path] = document
        
        self.root.document.Child.Content = document
        self.root.document.Child.ScrollToVerticalOffset(0)
        self.focus_text_box()

    
    def setup_parts(self):
        with open('docs/list.txt') as handle:
            items = handle.readlines()

        items = ['Index'] + items
        self.topCombobox = topCombobox = self.root.topComboBoxPart
        self.bottomCombobox = bottomCombobox = self.root.bottomComboBoxPart
        for combobox in topCombobox, bottomCombobox:
            for item in items:
                boxitem = ComboBoxItem()
                boxitem.Content = item
                boxitem.Height = 25
                combobox.Items.Add(boxitem)
            
        topCombobox.SelectionChanged += self.on_change_top_part
        bottomCombobox.SelectionChanged += self.on_change_bottom_part
        
            

    def on_change_top_part(self, sender, event):
        index = self.topCombobox.SelectedIndex
        self.bottomCombobox.SelectionChanged -= self.on_change_bottom_part
        self.bottomCombobox.SelectedIndex = index
        self.bottomCombobox.SelectionChanged += self.on_change_bottom_part
        self.change_document(index, 0)
        
    def on_change_bottom_part(self, sender, event):
        index = self.bottomCombobox.SelectedIndex
        self.topCombobox.SelectionChanged -= self.on_change_top_part
        self.topCombobox.SelectedIndex = index
        self.topCombobox.SelectionChanged += self.on_change_top_part
        self.change_document(index, 0)

    
    def on_change_top_page(self, sender, event):
        pass
    
    def on_change_bottom_page(self, sender, event):
        pass


"""

def first(sender, event):
    topCombobox.SelectedIndex = 0
def last(sender, event):
    topCombobox.SelectedIndex = len(combobox.Items) - 1
def next(sender, event):
    current = combobox.SelectedIndex
    topCombobox.SelectedIndex = min(current + 1, len(combobox.Items) - 1)
def prev(sender, event):
    current = combobox.SelectedIndex
    topCombobox.SelectedIndex = max(current - 1, 0)
    
    
root.topFirst.Click += first
root.bottomFirst.Click += first
root.topLast.Click += last
root.bottomLast.Click += last
root.topNext.Click += next
root.bottomNext.Click += next
root.topPrev.Click += prev
root.bottomPrev.Click += prev


page = 0
bookmark = HtmlPage.Window.CurrentBookmark.lower()
if bookmark.startswith('page'):
    try:
        page = int(bookmark[4:])
    except ValueError:
        pass
    else:
        page = min((page - 1), len(combobox.Items) - 1)
        page = max(page, 0)
        
topCombobox.SelectedIndex = page
"""