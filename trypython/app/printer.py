
from consoletextbox import get_console_block
from context import ps1, ps2
from utils import always_invoke, invoke

class StatefulPrinter(object):
    def __init__(self, parent, scroller):
        self.block = None
        self.parent = parent
        self.scroller = scroller
    
    @invoke
    def clear(self):
        self.parent.Children.Clear()
        
    @invoke
    def write(self, data):
        if self.block is None:
            self.block = get_console_block()
            self.parent.Children.Add(self.block)
            
        block = self.block
        if data.endswith('\n'):
            data = data[:-1]
            self.block = None
        
        block.Text += data
    
    def print_new(self, data):
        if self.block is not None:
            self.block = None
        if not data.endswith('\n'):
            data += '\n'
        self.write(data)

    def print_lines(self, data):
        lines = data.replace('\r\n', '\n').replace('\r', '\n').split('\n')
        lines[0] = ps1 + lines[0]
        lines[1:] = [ps2 + line for line in lines[1:]]
        self.print_new('\n'.join(lines))
    
    @always_invoke
    def scroll(self):
        scroller = self.scroller
        if scroller.ScrollableHeight > 0:
            scroller.ScrollToVerticalOffset(scroller.ScrollableHeight + scroller.ActualHeight)

