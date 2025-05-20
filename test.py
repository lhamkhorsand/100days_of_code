import sys
class Tag(object):
    def __init__(self, name, content, **att ):
        self.name = name
        self.start=f'<{name}>'
        self.end = f'</{name}>'
        self.content = content
        self.attrib= []

        if att:
            for k,v in att.items():
                self.attrib.append(f"{k} : '{v}'")
            att_str= ','.join(self.attrib)
            self.start =f'<{name} {att_str}>'



    def __str__(self):
        return f'{self.start} {self.content} {self.end}'

class Doctype(Tag):
    def __init__(self, version):
        if version == 1:
            name = '!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" ' \
                   '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"'
        elif version == 4:
            name = '!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" ' \
                   '"http://www.w3.org/TR/html4/loose.dtd"'
        elif version == 5:
            name = '!DOCTYPE html'
        else:
            print('HTML Version is not accepted')
            sys.exit(-1)
        super().__init__(name=name, content = '')

    def __str__(self):
        return f'{self.start}'


class Head(Tag):
    def __init__(self):
        super().__init__(name='head', content= '')
        self.content =[]

    def __str__(self):
        return f'{self.start}{self.end}'

    def add_content(self, name, closing, **at):
        cont = Tag()


if __name__ == '__main__' :
    t_test = Tag('myname', 'my content', filan='f', bisar= 'b' )

    print(t_test.attrib)
    print(t_test)

    d_test = Doctype(4)
    print(d_test)

    h_test= Head()
    print(h_test)