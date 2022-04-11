from typing import Text
import sys
class LSystem:

    def __init__(self, filename=None):
        # self.filename 
        self.rules = []
        self.baseString = ''
        if filename != None:
            self.read(filename)

    def setBase(self, newBase):
        '''set the base to the new base'''
        self.base = newBase
    
    def getBase(self):
        '''returns self.base'''
        return self.base
    
    def getRule(self, ruleIdx):
        return self.rules[ruleIdx]
    
    def addRule(self, newRule):
        '''Appends the new rules to the self.rules'''
        self.rules.append(newRule)
    
    def numRules(self):
        '''Returns the number of replacement rules currently in the L-System'''
        return len(self.rules)

    def read(self, filename):
        '''reads the L-system base string and 1+ rules from a text file. Stores the data in the instance variables in the 
        constructor in the format:
        
        base string: str.
        e.g. 'F-F-F-F'

        replacement rules: list of 2 element sublists.
        e.g. '[['F',  'FF-F+F-F-FF']] for one rule

        Parameters:
        filename: str. Filename of the L-syste, text file with the base string and 1+ replacement rules
        '''
        openFile = open(filename, 'r')
        for line in openFile:
            words = line.split()
            print(words[1:])
            if words[0] == 'base':
                self.setBase(words[1])
            if words[0] == 'rule':
                # self.addRule(words[1:])
                self.addRule(words[1:])
        openFile.close()
        '''Check if you can use while loop and readline() for this side of the code'''

    def replace(self, currString):
        '''Applies the full set of replacement rules to current 'base' L-system string 'currstring' '''
        newString = ''
        for c in currString:
            found = False
            for rule in self.rules:
                if rule[0] == c:
                    newString += rule[1]
                    found = True
                    break
                if not found:
                    newString += c
        return newString



    def buildString(self, iterations):
        '''Starting with the base string, apply the L-System replacement rules for 'n' iterations. '''
        ourString = self.base
        for i in range(iterations):
            ourString = self.replace(ourString)

        return ourString

   
def main(argv):
    if len(argv) < 2:
        print('usage: lsystem.py <filename>')
        exit()
    filename = argv[1]
    iterations = 2


    lsys = LSystem()
    lsys.read(filename)
    print(lsys)
    print(lsys.getBase())

    for i in range(lsys.numRules()):
        rule = lsys.getRule(i)
        print( rule[0] + '->' + rule[1] )

       

    lstring = lsys.buildString(iterations)
    print(lstring)

if __name__ == '__main__':
    main(sys.argv)

    