from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': '/powershell/management/Memory-spasm',

            'Author': ['@Homjxie'],

            'Description': ('Create spasm and consumption in memory and anxiety .'),

            'Background' : True,

            'OutputExtension' : None,

            'NeedsAdmin' : True,

            'OpsecSafe' : True,

            'Language' : 'powershell',

            'MinLanguageVersion' : '2',

            'Comments': [
                'https://twitter.com/GihadAlkmaty'
            ]
        }

         
        self.options = {
            
            
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

       
        self.mainMenu = mainMenu

        for param in params:
          
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value


    def generate(self):

        moduleName = self.info["Name"]

         
        moduleSource = self.mainMenu.installPath + "/data/module_source/management/Memory-spasm.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode

        script += "\nwio.sh"

        for option,values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])
	script += ' | Out-String | %{$_ + \"`n\"};"`n'+str(moduleName)+' completed!"'
   		    
        return script
