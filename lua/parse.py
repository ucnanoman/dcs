def loads(tablestr):

    class Parser():

        def __init__(self, buffer):
            self.buffer = buffer
            self.buflen = len(buffer)
            self.pos = 0

        def value(self):
            self.eatWS()

            if self.buffer[self.pos] == '{':
                return self.object()
            elif self.buffer[self.pos] == '"':
                return self.string()
            elif self.char().isnumeric() or self.char() == '-':
                return self.number()
            else:  # varname
                varname = self.eatvarname()
                if varname == 'false' or varname == 'true':
                    return varname == 'true'
                self.eatWS()
                if not self.eob() and self.buffer[self.pos] == '=':
                    self.pos += 1
                    return {varname: self.value()}
                else:
                    print("syntax ERROR:", varname, self.buffer[self.pos])

            return {}

        def string(self):
            if self.char() != '"':
                print('string parse error not starting with "')
                return ''

            state = 0
            s = ''
            while state != 1:
                if self.advance():
                    print('unexpected end of buffer')
                    return ''

                c = self.char()
                if state == 0:
                    if c == '"':
                        state = 1
                        self.advance()
                    elif c == '\\':
                        state = 2
                    else:
                        s += c
                if state == 2:
                    s += c
                    state = 0
            return s

        def number(self):
            n = ''
            sign = 1
            if self.char() == '-':
                sign = -1
                if self.advance():
                    print("unexpected end of buffer")

            while (not self.eob() and
                    (self.char().isnumeric() or self.char() == '.' or
                        self.char().lower() == 'e')):
                n += self.char()
                self.advance()

            return float(n) * sign

        def object(self):
            d = {}
            if self.char() != '{':
                print('object not starting with {')
                return {}

            if self.advance():
                print("unexpected end of buffer")

            self.eatWS()

            array = False

            while self.char() != '}':
                self.eatWS()

                if self.char() != '[':
                    print("object expected '[' got {char}'".format(char=self.char()))
                    return {}

                if self.advance():
                    print("unexpected end of buffer")
                    return {}

                self.eatWS()
                if self.char() == '"':
                    key = self.string()
                else:
                    key = str(self.number())
                    array = True

                if self.eob():
                    print("unexpected end of buffer")
                    return {}

                self.eatWS()

                if self.char() != ']':
                    print("object unexpected '{char}'".format(char=self.char()))
                    return {}

                if self.advance():
                    print("unexpected end of buffer")
                    return {}

                self.eatWS()

                if self.char() != '=':
                    print("object expected '=' got '{char}'".format(char=self.char()))
                    return {}

                if self.advance():
                    print("unexpected end of buffer")
                    return {}

                val = self.value()

                self.eatWS()

                d[key] = val
                # print(key, ':', val)

                if self.char() == '}':
                    break
                elif self.char() == ',':
                    if self.advance():
                        print("unexpected end of buffer")
                        return {}
                    self.eatWS()
                else:
                    print("object unexpected '{char}'".format(char=self.char()))
                    return {}

            self.advance()

            if array:
                return [d[k] for k in sorted(d)]

            return d

        def eatvarname(self):
            varname = ''
            while (not self.eob()) and self.buffer[self.pos].isalnum():
                varname += self.buffer[self.pos]
                self.pos += 1

            return varname

        def eatComment(self):
            if self.char() == '-' and self.pos + 1 < self.buflen and self.buffer[self.pos + 1] == '-':
                while not self.eob() and self.char() != '\n':
                    self.advance()

        def eatWS(self):
            self.eatComment()
            while not self.eob() and self.buffer[self.pos].isspace():
                self.pos += 1
                self.eatComment()

        def eob(self):
            return self.pos >= self.buflen

        def char(self):
            return self.buffer[self.pos]

        def advance(self):
            self.pos += 1
            return self.eob()

    p = Parser(tablestr)
    return p.value()
