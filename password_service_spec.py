# -*- coding: utf-8 -*-

from mamba import description, context, it
from doublex import Spy
from expects import expect
from doublex_expects import have_been_called

from passlib import pwd

# ----------

class PasswordService(object):
    def __init__(self, password_generator):
        self._password_generator = password_generator

    def generate(self):
        return self._password_generator.genword()

# ----------


with description('Password Service Specs') as self:
    with context('generate password for (happy path)'):
        with it('calls passlib library to generate random password'):
            # self.password_generator = Spy(pwd) # Fails
            self.password_generator = Spy()
            self.password_service = PasswordService(self.password_generator)

            self.password_service.generate()

            expect(self.password_generator.genword).to(have_been_called)
